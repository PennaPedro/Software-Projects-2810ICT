"""Simple user interface for the XPower Household Tariff Analysis prototype."""

from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from src.xpower.data_import import load_electricity_data, DataImportError
from src.xpower.tariffs import flat_bill, tiered_bill, tou_bill
from src.xpower.billing import (
    compare_tariffs,
    calculate_savings,
    cost_saving_suggestion,
)
from src.xpower.visualisation import (
    usage_line_chart,
    bill_comparison_chart,
)


class XPowerApp(tk.Tk):
    """Main XPower application window."""

    def __init__(self):
        super().__init__()

        self.title("XPower - Household Tariff Analysis")
        self.geometry("1050x700")
        self.minsize(900, 600)

        self.data = None
        self.comparison = None

        self._create_variables()
        self._create_style()
        self._create_interface()

    def _create_variables(self):
        """Create variables used by the interface."""

        # File information
        self.file_name = tk.StringVar(value="No file selected")
        self.data_summary = tk.StringVar(
            value="Upload a CSV or Excel file to begin."
        )

        # Flat Rate
        self.flat_rate = tk.StringVar(value="0.25")
        self.flat_fee = tk.StringVar(value="10.00")

        # Time-of-Use
        self.peak_rate = tk.StringVar(value="0.40")
        self.shoulder_rate = tk.StringVar(value="0.25")
        self.off_peak_rate = tk.StringVar(value="0.15")
        self.tou_fee = tk.StringVar(value="10.00")

        self.peak_start = tk.StringVar(value="18")
        self.peak_end = tk.StringVar(value="22")
        self.off_peak_start = tk.StringVar(value="22")
        self.off_peak_end = tk.StringVar(value="7")

        # Tiered
        self.tier1_limit = tk.StringVar(value="100")
        self.tier1_rate = tk.StringVar(value="0.20")

        self.tier2_limit = tk.StringVar(value="300")
        self.tier2_rate = tk.StringVar(value="0.30")

        self.tier3_rate = tk.StringVar(value="0.40")
        self.tiered_fee = tk.StringVar(value="10.00")

        # Results
        self.best_tariff = tk.StringVar(value="-")
        self.best_cost = tk.StringVar(value="-")
        self.savings = tk.StringVar(value="-")
        self.suggestion = tk.StringVar(
            value="Calculate the tariffs to see a suggestion."
        )

    def _create_style(self):
        """Create simple styles for the interface."""

        style = ttk.Style(self)

        style.configure(
            "Title.TLabel",
            font=("Arial", 22, "bold"),
        )

        style.configure(
            "Heading.TLabel",
            font=("Arial", 14, "bold"),
        )

        style.configure(
            "Result.TLabel",
            font=("Arial", 16, "bold"),
        )

    def _create_interface(self):
        """Create the four main interface screens."""

        header = ttk.Frame(self, padding=15)
        header.pack(fill="x")

        ttk.Label(
            header,
            text="XPower Household Tariff Analysis",
            style="Title.TLabel",
        ).pack(anchor="w")

        ttk.Label(
            header,
            text="Upload your electricity usage and compare household tariffs.",
        ).pack(anchor="w", pady=(4, 0))

        self.tabs = ttk.Notebook(self)
        self.tabs.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15),
        )

        self.upload_tab = ttk.Frame(self.tabs, padding=20)
        self.configure_tab = ttk.Frame(self.tabs, padding=20)
        self.calculate_tab = ttk.Frame(self.tabs, padding=20)
        self.results_tab = ttk.Frame(self.tabs, padding=20)

        self.tabs.add(
            self.upload_tab,
            text="1. Upload Data",
        )

        self.tabs.add(
            self.configure_tab,
            text="2. Configure Tariffs",
        )

        self.tabs.add(
            self.calculate_tab,
            text="3. Calculate & Compare",
        )

        self.tabs.add(
            self.results_tab,
            text="4. Results & Savings",
        )

        self._build_upload_tab()
        self._build_configure_tab()
        self._build_calculate_tab()
        self._build_results_tab()

    # ---------------------------------------------------------
    # SCREEN 1 - UPLOAD
    # ---------------------------------------------------------

    def _build_upload_tab(self):
        ttk.Label(
            self.upload_tab,
            text="Upload Electricity Data",
            style="Heading.TLabel",
        ).pack(anchor="w")

        ttk.Label(
            self.upload_tab,
            text=(
                "Select a CSV or Excel file containing a timestamp "
                "and electricity usage column."
            ),
        ).pack(anchor="w", pady=(5, 20))

        upload_box = ttk.LabelFrame(
            self.upload_tab,
            text="Electricity Usage File",
            padding=20,
        )
        upload_box.pack(fill="x")

        ttk.Label(
            upload_box,
            textvariable=self.file_name,
        ).pack(anchor="w", pady=(0, 10))

        ttk.Button(
            upload_box,
            text="Select CSV / Excel File",
            command=self.select_file,
        ).pack(anchor="w")

        summary_box = ttk.LabelFrame(
            self.upload_tab,
            text="Imported Data Summary",
            padding=20,
        )
        summary_box.pack(
            fill="x",
            pady=20,
        )

        ttk.Label(
            summary_box,
            textvariable=self.data_summary,
            justify="left",
        ).pack(anchor="w")

        ttk.Button(
            self.upload_tab,
            text="Continue to Tariff Configuration",
            command=lambda: self.tabs.select(self.configure_tab),
        ).pack(anchor="e", pady=10)

    # ---------------------------------------------------------
    # SCREEN 2 - CONFIGURATION
    # ---------------------------------------------------------

    def _build_configure_tab(self):
        ttk.Label(
            self.configure_tab,
            text="Configure Tariffs",
            style="Heading.TLabel",
        ).pack(anchor="w")

        ttk.Label(
            self.configure_tab,
            text=(
                "You can use the example values below or change them "
                "before calculating the bills."
            ),
        ).pack(anchor="w", pady=(5, 15))

        container = ttk.Frame(self.configure_tab)
        container.pack(
            fill="both",
            expand=True,
        )

        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=1)
        container.columnconfigure(2, weight=1)

        # Flat Rate
        flat_box = ttk.LabelFrame(
            container,
            text="Flat Rate",
            padding=15,
        )
        flat_box.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=5,
        )

        self._entry_row(
            flat_box,
            "Rate ($/kWh)",
            self.flat_rate,
            0,
        )

        self._entry_row(
            flat_box,
            "Fixed Fee ($)",
            self.flat_fee,
            1,
        )

        # Time-of-Use
        tou_box = ttk.LabelFrame(
            container,
            text="Time-of-Use",
            padding=15,
        )
        tou_box.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=5,
        )

        self._entry_row(tou_box, "Peak Rate", self.peak_rate, 0)
        self._entry_row(tou_box, "Shoulder Rate", self.shoulder_rate, 1)
        self._entry_row(tou_box, "Off-Peak Rate", self.off_peak_rate, 2)
        self._entry_row(tou_box, "Fixed Fee", self.tou_fee, 3)

        self._entry_row(tou_box, "Peak Start Hour", self.peak_start, 4)
        self._entry_row(tou_box, "Peak End Hour", self.peak_end, 5)

        self._entry_row(
            tou_box,
            "Off-Peak Start",
            self.off_peak_start,
            6,
        )

        self._entry_row(
            tou_box,
            "Off-Peak End",
            self.off_peak_end,
            7,
        )

        # Tiered
        tiered_box = ttk.LabelFrame(
            container,
            text="Tiered",
            padding=15,
        )
        tiered_box.grid(
            row=0,
            column=2,
            sticky="nsew",
            padx=5,
        )

        self._entry_row(
            tiered_box,
            "Tier 1 Limit",
            self.tier1_limit,
            0,
        )

        self._entry_row(
            tiered_box,
            "Tier 1 Rate",
            self.tier1_rate,
            1,
        )

        self._entry_row(
            tiered_box,
            "Tier 2 Limit",
            self.tier2_limit,
            2,
        )

        self._entry_row(
            tiered_box,
            "Tier 2 Rate",
            self.tier2_rate,
            3,
        )

        self._entry_row(
            tiered_box,
            "Tier 3 Rate",
            self.tier3_rate,
            4,
        )

        self._entry_row(
            tiered_box,
            "Fixed Fee",
            self.tiered_fee,
            5,
        )

        ttk.Button(
            self.configure_tab,
            text="Continue to Calculation",
            command=lambda: self.tabs.select(self.calculate_tab),
        ).pack(anchor="e", pady=15)

    def _entry_row(self, parent, label, variable, row):
        """Create a label and entry field."""

        ttk.Label(
            parent,
            text=label,
        ).grid(
            row=row,
            column=0,
            sticky="w",
            pady=4,
        )

        ttk.Entry(
            parent,
            textvariable=variable,
            width=12,
        ).grid(
            row=row,
            column=1,
            sticky="e",
            padx=(10, 0),
            pady=4,
        )

    # ---------------------------------------------------------
    # SCREEN 3 - CALCULATE
    # ---------------------------------------------------------

    def _build_calculate_tab(self):
        ttk.Label(
            self.calculate_tab,
            text="Calculate and Compare Tariffs",
            style="Heading.TLabel",
        ).pack(anchor="w")

        ttk.Label(
            self.calculate_tab,
            text=(
                "XPower will calculate Flat Rate, Time-of-Use "
                "and Tiered bills using the uploaded electricity data."
            ),
        ).pack(anchor="w", pady=(5, 20))

        summary_box = ttk.LabelFrame(
            self.calculate_tab,
            text="Electricity Data",
            padding=20,
        )
        summary_box.pack(fill="x")

        ttk.Label(
            summary_box,
            textvariable=self.data_summary,
            justify="left",
        ).pack(anchor="w")

        ttk.Button(
            self.calculate_tab,
            text="Calculate & Compare Tariffs",
            command=self.calculate,
        ).pack(
            pady=30,
        )

    # ---------------------------------------------------------
    # SCREEN 4 - RESULTS
    # ---------------------------------------------------------

    def _build_results_tab(self):
        ttk.Label(
            self.results_tab,
            text="Results and Savings",
            style="Heading.TLabel",
        ).pack(anchor="w")

        result_summary = ttk.Frame(self.results_tab)
        result_summary.pack(
            fill="x",
            pady=15,
        )

        result_summary.columnconfigure(0, weight=1)
        result_summary.columnconfigure(1, weight=1)
        result_summary.columnconfigure(2, weight=1)

        self._result_box(
            result_summary,
            "Best Tariff",
            self.best_tariff,
            0,
        )

        self._result_box(
            result_summary,
            "Estimated Cost",
            self.best_cost,
            1,
        )

        self._result_box(
            result_summary,
            "Possible Saving",
            self.savings,
            2,
        )

        table_box = ttk.LabelFrame(
            self.results_tab,
            text="Tariff Comparison",
            padding=10,
        )
        table_box.pack(
            fill="x",
            pady=10,
        )

        self.result_table = ttk.Treeview(
            table_box,
            columns=("tariff", "cost"),
            show="headings",
            height=3,
        )

        self.result_table.heading(
            "tariff",
            text="Tariff",
        )

        self.result_table.heading(
            "cost",
            text="Estimated Bill",
        )

        self.result_table.pack(fill="x")

        suggestion_box = ttk.LabelFrame(
            self.results_tab,
            text="Cost-Saving Suggestion",
            padding=15,
        )
        suggestion_box.pack(
            fill="x",
            pady=10,
        )

        ttk.Label(
            suggestion_box,
            textvariable=self.suggestion,
            wraplength=850,
            justify="left",
        ).pack(anchor="w")

        button_frame = ttk.Frame(self.results_tab)
        button_frame.pack(
            fill="x",
            pady=15,
        )

        ttk.Button(
            button_frame,
            text="View Usage Chart",
            command=self.show_usage_chart,
        ).pack(
            side="left",
            padx=(0, 10),
        )

        ttk.Button(
            button_frame,
            text="View Bill Comparison Chart",
            command=self.show_bill_chart,
        ).pack(side="left")

    def _result_box(self, parent, title, variable, column):
        """Create a result summary box."""

        box = ttk.LabelFrame(
            parent,
            text=title,
            padding=15,
        )

        box.grid(
            row=0,
            column=column,
            sticky="nsew",
            padx=5,
        )

        ttk.Label(
            box,
            textvariable=variable,
            style="Result.TLabel",
        ).pack()

    # ---------------------------------------------------------
    # DATA IMPORT
    # ---------------------------------------------------------

    def select_file(self):
        """Allow the user to select and import electricity data."""

        file_path = filedialog.askopenfilename(
            title="Select Electricity Usage File",
            filetypes=[
                ("Electricity Data", "*.csv *.xlsx"),
                ("CSV Files", "*.csv"),
                ("Excel Files", "*.xlsx"),
            ],
        )

        if not file_path:
            return

        try:
            self.data = load_electricity_data(file_path)

        except DataImportError as error:
            messagebox.showerror(
                "Data Import Error",
                str(error),
            )
            return

        self.file_name.set(Path(file_path).name)

        rows = len(self.data)
        total_usage = self.data["usage_kwh"].sum()
        start_date = self.data["timestamp"].min()
        end_date = self.data["timestamp"].max()

        summary = (
            f"Records: {rows}\n"
            f"Total Usage: {total_usage:.2f} kWh\n"
            f"From: {start_date}\n"
            f"To: {end_date}"
        )

        self.data_summary.set(summary)

        messagebox.showinfo(
            "Data Imported",
            "Electricity usage data was imported successfully.",
        )

    # ---------------------------------------------------------
    # BILL CALCULATION
    # ---------------------------------------------------------

    def calculate(self):
        """Calculate and compare all three tariffs."""

        if self.data is None:
            messagebox.showerror(
                "Missing Data",
                "Please upload electricity usage data first.",
            )
            return

        try:
            total_usage = float(self.data["usage_kwh"].sum())

            flat_result = flat_bill(
                total_usage,
                float(self.flat_rate.get()),
                float(self.flat_fee.get()),
            )

            tou_result = tou_bill(
                self.data,
                peak_rate=float(self.peak_rate.get()),
                shoulder_rate=float(self.shoulder_rate.get()),
                off_peak_rate=float(self.off_peak_rate.get()),
                fee=float(self.tou_fee.get()),
                peak_start=int(self.peak_start.get()),
                peak_end=int(self.peak_end.get()),
                off_peak_start=int(self.off_peak_start.get()),
                off_peak_end=int(self.off_peak_end.get()),
            )

            tiered_result = tiered_bill(
                total_usage,
                t1_limit=float(self.tier1_limit.get()),
                t1_rate=float(self.tier1_rate.get()),
                t2_limit=float(self.tier2_limit.get()),
                t2_rate=float(self.tier2_rate.get()),
                t3_rate=float(self.tier3_rate.get()),
                fee=float(self.tiered_fee.get()),
            )

        except ValueError:
            messagebox.showerror(
                "Invalid Tariff Settings",
                "Please enter valid numbers for all tariff settings.",
            )
            return

        results = [
            flat_result,
            tou_result,
            tiered_result,
        ]

        for result in results:
            if isinstance(result, str) and result.startswith("Error"):
                messagebox.showerror(
                    "Calculation Error",
                    result,
                )
                return

        self.comparison = compare_tariffs(
            flat_result,
            tou_result,
            tiered_result,
        )

        if isinstance(self.comparison, str):
            messagebox.showerror(
                "Comparison Error",
                self.comparison,
            )
            return

        saving = calculate_savings(self.comparison)
        advice = cost_saving_suggestion(self.comparison)

        self.best_tariff.set(
            self.comparison["cheapest_tariff"]
        )

        self.best_cost.set(
            f"${self.comparison['cheapest_cost']:.2f}"
        )

        self.savings.set(
            f"${saving:.2f}"
        )

        self.suggestion.set(advice)

        # Clear previous table results.
        for item in self.result_table.get_children():
            self.result_table.delete(item)

        for tariff, cost in self.comparison["bills"].items():
            self.result_table.insert(
                "",
                "end",
                values=(
                    tariff,
                    f"${cost:.2f}",
                ),
            )

        self.tabs.select(self.results_tab)

    # ---------------------------------------------------------
    # CHARTS
    # ---------------------------------------------------------

    def show_usage_chart(self):
        """Display the electricity usage line chart."""

        if self.data is None:
            messagebox.showerror(
                "Missing Data",
                "Please upload electricity data first.",
            )
            return

        result = usage_line_chart(self.data)

        if isinstance(result, str):
            messagebox.showerror(
                "Chart Error",
                result,
            )
            return

        result.show()

    def show_bill_chart(self):
        """Display the tariff comparison chart."""

        if self.comparison is None:
            messagebox.showerror(
                "Missing Results",
                "Please calculate the tariff results first.",
            )
            return

        result = bill_comparison_chart(
            self.comparison
        )

        if isinstance(result, str):
            messagebox.showerror(
                "Chart Error",
                result,
            )
            return

        result.show()


def run_app():
    """Start the XPower user interface."""

    app = XPowerApp()
    app.mainloop()


if __name__ == "__main__":
    run_app()
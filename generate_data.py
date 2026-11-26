"""Dataset generators for the PLP Week 4 assignment.

Run:  python generate_data.py
Writes student_performance.csv (seed 55) and duka_sales.csv (seed 2026).
"""
import numpy as np, pandas as pd

# ---------------------------------------------------------------------------
# Engagement 1 - Student performance (seed 55) -> student_performance.csv
# ---------------------------------------------------------------------------
rng = np.random.default_rng(55)

n = 1200

students = pd.DataFrame({

    "student_id": range(1, n + 1),

    "county": rng.choice(["Nairobi", "Kisumu", "Nakuru",

                          "Mombasa", "Nyeri", "Turkana"], n),

    "school_type": rng.choice(["Public", "Private"], n, p=[0.75, 0.25]),

    "gender": rng.choice(["F", "M"], n),

    "attendance_rate": rng.beta(8, 2, n).round(2),

    "study_hours": rng.gamma(2.5, 2.0, n).round(1),

})

base = (35 + 30 * students["attendance_rate"] + 2.2 * students["study_hours"]

        + np.where(students["school_type"] == "Private", 6, 0))

students["math"] = (base + rng.normal(0, 8, n)).clip(0, 100).round(0)

students["english"] = (base + rng.normal(3, 7, n)).clip(0, 100).round(0)

students["science"] = (base + rng.normal(-2, 9, n)).clip(0, 100).round(0)

students.to_csv("student_performance.csv", index=False)


# ---------------------------------------------------------------------------
# Engagement 2 - Duka Electronics (seed 2026) -> duka_sales.csv
# ---------------------------------------------------------------------------
rng = np.random.default_rng(2026)
n = 1000
products = {"Phone": 15000, "Laptop": 65000, "Headphones": 2500,
            "Tablet": 28000, "Charger": 1200}

sales = pd.DataFrame({
    "order_id": range(1001, 1001 + n),
    "order_date": pd.to_datetime("2026-01-01")
                  + pd.to_timedelta(rng.integers(0, 180, n), unit="D"),
    "branch": rng.choice(["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Eldoret"], n,
                         p=[0.4, 0.2, 0.15, 0.15, 0.1]),
    "product": rng.choice(list(products), n),
    "quantity": rng.integers(1, 6, n),
    "channel": rng.choice(["In-store", "Online", "Phone order"], n,
                          p=[0.55, 0.35, 0.10]),
})

sales["unit_price"] = sales["product"].map(products)

sales.to_csv("duka_sales.csv", index=False)

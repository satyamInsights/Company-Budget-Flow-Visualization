# ==========================================
# INSTALL (Only for Colab)
# ==========================================
# !pip install plotly pandas

# ==========================================
# IMPORT LIBRARIES
# ==========================================
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio

# Force browser rendering (VS Code ke liye useful)
pio.renderers.default = "browser"

# ==========================================
# SANKEY DIAGRAM DATA
# ==========================================

labels = [
    "Company",
    "HR",
    "IT",
    "Marketing",
    "Finance",
    "Recruitment",
    "Training",
    "Infrastructure",
    "Software",
    "Digital Ads",
    "Events",
    "Audit",
    "Investment"
]

# Source Nodes
source = [
    0, 0, 0, 0,
    1, 1,
    2, 2,
    3, 3,
    4, 4
]

# Target Nodes
target = [
    1, 2, 3, 4,
    5, 6,
    7, 8,
    9, 10,
    11, 12
]

# Budget Flow
value = [
    50000,
    120000,
    80000,
    70000,
    25000,
    25000,
    70000,
    50000,
    50000,
    30000,
    30000,
    40000
]

# Percentage Calculation
total = sum(value)

percentage = [
    round((v / total) * 100, 2)
    for v in value
]

# ==========================================
# SANKEY CHART
# ==========================================

sankey_fig = go.Figure(
    go.Sankey(
        node=dict(
            pad=20,
            thickness=25,
            line=dict(color="black", width=1),
            label=labels,
            color="royalblue"
        ),

        link=dict(
            source=source,
            target=target,
            value=value,
            color="lightblue",
            customdata=percentage,

            hovertemplate=
            "<b>Flow Value:</b> ₹%{value}<br>" +
            "<b>Contribution:</b> %{customdata}%<extra></extra>"
        )
    )
)

sankey_fig.update_layout(
    title="Interactive Company Budget Flow (Sankey Diagram)",
    title_x=0.5,
    template="plotly_dark",
    font_size=12,
    height=700
)

sankey_fig.show()

# ==========================================
# SUNBURST DATA
# ==========================================

sunburst_df = pd.DataFrame({
    "Department": [
        "HR",
        "HR",
        "IT",
        "IT",
        "Marketing",
        "Marketing",
        "Finance",
        "Finance"
    ],

    "Sub_Department": [
        "Recruitment",
        "Training",
        "Infrastructure",
        "Software",
        "Digital Ads",
        "Events",
        "Audit",
        "Investment"
    ],

    "Budget": [
        25000,
        25000,
        70000,
        50000,
        50000,
        30000,
        30000,
        40000
    ]
})

# ==========================================
# SUNBURST CHART
# ==========================================

sunburst_fig = px.sunburst(
    sunburst_df,
    path=["Department", "Sub_Department"],
    values="Budget",
    color="Budget",
    color_continuous_scale="Blues",
    title="Interactive Budget Hierarchy (Sunburst Chart)"
)

sunburst_fig.update_traces(
    hovertemplate=
    "<b>%{label}</b><br>" +
    "Budget: ₹%{value}<br>" +
    "<extra></extra>"
)

sunburst_fig.update_layout(
    template="plotly_dark",
    title_x=0.5,
    height=700
)

sunburst_fig.show()
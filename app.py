#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Alexandru Schneider
# Created Date: 23. 11. 2021
# =============================================================================
# Dashboard App about Olympia data
# =============================================================================

# =============================================================================
# Imports
# =============================================================================
import pandas as pd
import dash
from dash import html, dcc, Input, Output
import plotly.express as px

def main():
    df = loadData()
    app = initApp()
    app.layout = html.Div(children=[html.H2("Dashboard Olympia Alex & André")])

    app.run_server(debug=True, host="0.0.0.0", port=9999)


if __name__ == "__main__":
    main()

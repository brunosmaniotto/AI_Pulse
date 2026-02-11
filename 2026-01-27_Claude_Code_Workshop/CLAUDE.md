# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the UC Berkeley D-Lab's Claude Code Workshop repository - educational materials for teaching AI-assisted coding with Claude Code CLI. The workshop demonstrates code generation, documentation, refactoring, and data consolidation tasks.

## Repository Structure

- **demo1_linear_regression/**: Code generation demo - builds OLS regression from CSV data
- **demo2_julia_documentation/**: Documentation demo - generates docs for DSGE.jl (Federal Reserve's Julia DSGE model)
- **demo3_refactoring/**: Refactoring demo - cleans up a messy PhD thesis codebase with hardcoded paths, repetitive code, poor organization
- **demo4_data_consolidation/**: Data merging demo with subagent verification using FRED, Michigan Survey, and SPF economic data
- **slides/**: Workshop presentation (LaTeX source and PDF)
- **assets/**: Example CLAUDE.md template for teaching

## Demo-Specific Notes

### Demo 1 (Linear Regression)
- Sample data: `productivity_study.csv` (coffee consumption vs productivity)
- `dry_run_results/` contains pre-generated example outputs

### Demo 2 (Julia Documentation)
- Requires downloading DSGE.jl from https://github.com/FRBNY-DSGE/DSGE.jl
- Place as `DSGE.jl-main/` in the demo folder

### Demo 3 (Refactoring)
- `messy_codebase/` intentionally contains poor practices for demonstration
- Issues include: hardcoded Windows paths, code duplication, mixed concerns

### Demo 4 (Data Consolidation)
- Requires downloading data from FRED, Michigan Survey, and SPF (see SOURCE.md)
- Data files excluded from git due to size

## Data File Handling

Large data files are excluded via .gitignore:
- Excel files (*.xls, *.xlsx, *.dta, *.rds)
- CSV files in demo4_data_consolidation/
- External codebases (DSGE.jl-main/, fred/, michigan/, spf/)

Exception: `demo1_linear_regression/productivity_study.csv` is tracked for demo purposes.

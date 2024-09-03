# MandVModeling Project README

[!NOTE]
This project is actively developed. Expect frequent updates and changes.

## Overview

MandVModeling is an open-source Python project for modeling and visualizing changepoint models. It provides tools for generating coordinates, plotting data, and analyzing trends in time series data. Borrows heavily from CUNY Building Performance Lab's `changepointmodel` Github repository.


## Table of Contents

1. [Project Structure](#project-structure)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Features](#features)
5. [Contributing](#contributing)
6. [License](#license)
7. [Acknowledgments](#acknowledgments)

## Project Structure

The project consists of several main components:

- `mandvmodeling/core`: Contains core classes and utilities
- `mandvmodeling/plotly_plotting`: Implements Plotly-based visualization tools
- `mandvmodeling/changepoint_models`: Provides implementations of different changepoint models

## Installation

## Usage

## Features

- Supports various changepoint models (two-parameter, three-parameter, four-parameter, five-parameter)
- Generates boundary coordinates and changepoint coordinates
- Provides Plotly-based visualization tools
- Handles time series data analysis

## Future Work

- [] Test the model coordinates parsers in `model_coordinates_parsers.py`
- [] Test the `PlotlyModelCoordinates`, `PlotlyRawDataCoordinates`, `PlotlyModelParameters`, `PlotlyRawDataParameters` dataclasses in the `plotly_parameters.py` file.
- [] Create test fixtures for the model coordinates parsers and the `PlotlyModelParameters` and `PlotlyRawDataParameters` dataclasses.
- [] Test every non-abstract-base-class class in `coordinates.py` and create relevant fixtures for these classes.
- [] Test and create fixtures for the `PlotlyParameterModelCoordinates` class in the `derive_model_coordinates.py` file.
- [] Test the `MandVModeling` class in the `estimator.py` file.
- [] Ensure that all of the `__init__.py` files in this repository have the relative imports
- [] Ensure that pydantic v2 is being used and is compatible with the entire package
- [] Ensure PEP 484 compliancy. Make sure everything has a specified type.
- [] Put up some badges on this readme to show relevant information about this package.
- [] [Use Github Actions to develop a Python workflow](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-python)

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the Python community for creating such powerful libraries like NumPy and Plotly.
- Inspiration drawn from various changepoint detection algorithms and visualizations.

---

This README provides an overview of the MandVModeling project structure, installation instructions, usage examples, features, contribution guidelines, license information, and acknowledgments. It serves as a starting point for users and contributors alike, providing essential information about the project's purpose, functionality, and how to engage with it.
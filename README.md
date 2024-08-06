# 3D-plant-phenotyping-measurement
Core modules:
plant_phenotyping.py: Contains core algorithms and functions.
data_processing.py: Processes input data, including reading, cleaning, preprocessing, etc.
visualization.py: Implements visualization functions, such as drawing 3D models, generating charts, etc.
model.py: If a machine learning model is involved, it is used to define the model structure.

Auxiliary modules:
utils.py: Contains some commonly used utility functions, such as reading configuration files, logging, etc.
constants.py: Defines constants, such as file paths, parameters, etc.
tests.py: Used to write unit tests.

Specific functional modules:
segmentation.py: implement image segmentation function.
feature_extraction.py: extract plant features.
measurement.py: perform specific measurements.
calibration.py: perform camera calibration.
registration.py: implement image registration.
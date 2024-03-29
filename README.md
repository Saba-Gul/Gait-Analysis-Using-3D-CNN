# Gait Recognition with 3D CNN

## Introduction
Gait recognition is a promising avenue for identification and authentication due to the uniqueness of individual strides. This project proposes a novel approach using 3D convolutional neural networks (3D CNN) to capture spatio-temporal features of gait sequences for robust recognition.

## Methodology
- **3D CNN Architecture**: The proposed network architecture employs a holistic approach using gait energy images (GEI) to capture shape and motion (Spatio-Temporal features) characteristics of human gait.
 
 ![Gait Analysis1](images/Proposed_framework.png "3D Convolutional Neural Network for Inter-class Subject Identification")

- **Dataset**: Evaluation was conducted on two publicly available datasets, OULP and CASIA-B, which exhibit substantial gender and age diversity.
  
 ![Gait Analysis2](images/CASIA-B_Dataset.png "Data-set Specifications CASIA-B")

 ![Gait Analysis3](images/OULP_Dataset.png "Data-set Specifications OULP")

- **Optimization Strategies**: Bayesian algorithms were explored to tune hyperparameters and enhance network performance.

 ![Gait Analysis4](images/HypOpt.png "Hyper-parameter tuning using bayesian optimization")

## Key Features
- Robust Gait Recognition: The optimized 3D CNN and GEI effectively capture unique gait characteristics despite challenging covariates such as change in speed, viewpoint, clothing, and carrying accessories.
- State-of-the-Art Results: Achieved state-of-the-art results on multi-views and multiple carrying conditions of subjects in the CASIA-B dataset.
  
 ![Gait Analysis7](images/Performance.png "Comparison of our framework with state of art models")
 
 ![Gait Analysis5](images/CASIAB_Results.png "Proposed network training results on CASIA-B dataset")

 ![Gait Analysis6](images/OULP_Results.png "Proposed network training results on OULP dataset")
 

 
## Future Directions
- Overcoming Overfitting: Address potential overfitting issues due to limited variance and frames per subject in the OULP dataset.
- Genetic Optimization Algorithms: Explore genetic optimization algorithms to further enhance performance.
- Real-life Scenarios: Extend the framework to practical environments by tackling more challenging real-life scenarios for person identification based on walking patterns.

## Usage
- Clone the repository.
- Install necessary dependencies.
- Execute the main script for gait recognition.

## Citation
Gul S., Malik M.I., Khan G.M., Shafait F. (2021) Multi-view Gait Recognition System using
Spatio-temporal Features and Deep learning, Expert Systems with Applications,115057, ISSN
0957-4174, https://doi.org/10.1016/j.eswa.2021.115057.



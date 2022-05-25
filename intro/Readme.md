[youtube](https://www.youtube.com/watch?v=s0uaFZSzwfI&list=PL3MmuxUbc_hIUISrluw_A7wDSmfOhErJK&index=2 )

_MLOps is a set of best practices for bringing Machine Learning to production._

## Machine Learning projects best practices can be categrized into 3 steps:

* Design -in the design steps askinng the question "is ML the right tool for solving our problem?"
For exampe if We want to predict the duration of a taxi trip. Do we need to use ML or can we used a simpler rule-based model?

* Train - if we do need ML, then we train and evaluate the best model.

* Operate - model deployment, management and monitoring.

## MLOps is helpful in all 3 stages.


## Environment setup

To setup a linux VM instance in GCP check the video link below to watch a video in to learn how to set.

<br>[youtube] (https://www.youtube.com/watch?v=ae-CV2KfoN0&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=13)

<br>This link shows how to make the configuration on AWS server
[youtube] (https://www.youtube.com/watch?v=IXSiYkP23zo&list=PL3MmuxUbc_hIUISrluw_A7wDSmfOhErJK&index=4 )

  
## The requirements for this course are:
* Docker and Docker Compose
Docker Desktop is recommended for download for both components.
* Anaconda (has Python 3.9,Jupyter notebook)
* IDE : VSCode 
<br>Using Visual Studio Code and the Remote - SSH extension
These requirements are not necessary but they make it much easier to connect to remote instances and redirect ports. Note: Any additional requirements will be listed as needed during the course.

## To go through the homework 
The homework requires need pandas, scikit-learn, fastparquet/pyarrow, matplotlib and seaborn. 
Homework link : 
* [Homework1](https://github.com/Ayanlola2002/mlops_zoomcamp/tree/main/intro)

The following videos also show how to train a model for the purpose of using it later in the course. They use the New York City's TLC Trip Record Data for training. 
* Training a model videos
[youtube](https://www.youtube.com/watch?v=iRunifGSHFc&list=PL3MmuxUbc_hIUISrluw_A7wDSmfOhErJK&index=6)

* Reading parquet files video
[youtube](https://www.youtube.com/watch?v=r94QjpX9vSE&list=PL3MmuxUbc_hIUISrluw_A7wDSmfOhErJK&index=4)

## Course structure outline
[youtube](https://www.youtube.com/watch?v=teP9KWkP6SM&list=PL3MmuxUbc_hIUISrluw_A7wDSmfOhErJK&index=6) 

Due to the nature of experimentation, data scientists who use Jupyter Notebooks to create models frequently do not follow best practices and are often unstructured: cells are re-run with slightly altered values, and earlier results may be lost, or the cell execution order may be inconsistent.

* Module 2: in this module we'll use tools like MLflow to create experiment trackers (such as the history of cells that we've rerun multiple times) and model registries (for storing the models we've created during the experiments).

* Module 3 covers orchestration and machine learning pipelines: we can break down our notebooks into separate identifiable steps and connect them using tools like Prefect and Kubeflow to create an ML pipeline that we can parametrize with the data and models we want and easily execute using tools like Prefect and Kubeflow.

* Serving the models is covered in Module 4: we'll learn how to deploy models in various methods.

* Model monitoring is covered in Module 5: we'll learn how to check whether our model is working properly, produce alerts for performance decreases and failures, and even automate retraining and redeploying models without human intervention.

* Best practices are covered in Module 6, such as how to properly maintain and package code, how to reliably deploy, and so on.

* Processes are covered in Module 7: we'll learn how to effectively communicate and collaborate with all stakeholders in a machine learning project (scientists, engineers, and so on).

# Maturity model








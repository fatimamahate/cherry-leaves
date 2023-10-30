![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Cherry Leaves - Mildew Detection

## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). The USer story is ficticious from the assesment handbook.However can be applied to real life. 
* The data has over 4000 images of cherry leaves that are either healthy or affected by powdery mildew. This can affect the profits of the farm since if the farmer is able to quickly identify an affected tree, they would be able to make a quick decision on what to do and can therefore focus efforts on a healthy tree.

## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis and how to validate?
* The unhealthy, mildewy leaves have marks which will allow to identify which leaves are healthy. This will allow for identification of each leaf.

## The rationale to map the business requirements to the Data Visualisations and ML tasks
### Requirement 1
* Display the 'mean/average' and 'standard deviation' images for mildew  and healthy leaves.
* Display the difference between each leaf
### Requirement 2
* Predict if the leaf is affected with mildew or not.

## ML Business Case
* This is primarily in the farming industry and also for city parks and green spaces. Cherry trees are common around the country however, for edible cherry trees and for farming, it is even more important to work out which trees are affected with powdery mildew and which aren't. Furthermore, by being able to save time in identifying mildewy leaves, it may be possible to increase profits by spending more time on frowing healthy trees. 
* A classification model will be used to identify the healthy leaves versus the leaves affected by powdery mildew.
* The images of the leaves have been provided.
* The client would require a dashboard for this.
* The aim would be to ensure correct classification of the mildewy and healthy leaves. 
* The classification model should have a >65% accuracy. 
  
## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items, that your dashboard library supports.
* Finally, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later, you chose another plot type).

## Unfixed Bugs


## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file. 


## Main Data Analysis and Machine Learning Libraries
* Numpy
* os 


## Credits 

* This project is based on the walkthrough project 1 which was taught by Gyan Shashwat. It was interesting to see similarities between both business requirements. You can find the Github Repository for the walkthrough project [here](https://github.com/Code-Institute-Solutions/WalkthroughProject01). 
* Furthermore, the assessment handbook was where this idea had come from along with the dataset which can be found in this [Kaggle Link](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)


### Content 


### Media

The images of leaves were in the dataset provided by Code Institute at this [link](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)



## Acknowledgements (optional)
* Thank the people that provided support throughout this project.

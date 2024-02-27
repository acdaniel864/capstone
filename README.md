# README - Why, Why, Wine
**Price Predictive Modelling and an Application for Consumer Wine Comparison**<br>
Capstone Project by Aaran Daniel<br>

## Intro:<br>
Not the first wine-based Data Science project and it won't be the last but this project puts a fresh twist on an industy subject to the interest of many a thirsty data-scientist. Over 50,000 wines are analysed in a project that is designed: 1. To shed light on what makes consumer wine expensive (or cheap) and; 2. To help consumers identify some delicious bargains. We could imagine a very basic approach to uncovering underpriced wines would be simply comparing rating to price. Yhose wines with a higher than avergae rating and a lower than price can be called 'good value'. This misses a crucial quesiton: "do consumers rate how good a wine is for its price or how good the wine is compared to all possible wines?" Through exploratory analysis and ** .

The end result will be a high-acccuracy price predictive model and an application designed for users to input wines and receive back similar wines, vintage comparisons and a measure of value. Helping the user decide if the wine they are interested in is overvalued, undervalued or just-right.<br> 

## Problem Statement:<br>
We look to understand what features are most predictive of wine prices and in doing so identify oppotiunities to purchase great wines at bargain prices.<br>

## Primary Aim:<br>
Using historical price data of wines develop a predictive model for prices and help consumers identify bargain wines.<br>

## Secondary Aims:
- Identify key price predictive features.<br>
- Investigate if a renowned reviewer having simply reviewed a wine can dictate value one way or another.<br>
- Find undervalued wines which match features of higher value wines but at a bargain price.<br>
- Identify region/vintages that are highly rated compared to others. <br>
- Suggest up-and-coming wines or producers that appear to be gaining in reputation and/or price.<br>
- **Build an application** which allows wine buyers to search a wines and returns recommended similar wines, previous vintage price/performance and an estimate of ideal drinking window.<br>
- Investigate the relationship between price and rating. Do consumers take into account the price before rating a wine or are all ratings equal?<br>

## Metric for Success
- A model that is able to predict prices to within 5% of actual price.<br>
- Functioning application that is able to take as input even wines not in the dataset.<br>


## Cleaned and Combined Dataset Data Dictionary:<br>


## Process

### 1. Data Collection
- **[Wine.com dataset](https://www.kaggle.com/datasets/salohiddindev/wine-dataset-scraping-from-wine-com):**
**Scrapped:** 02/11/23<br>
**Features:**<br>
Names: Name of the wine, grape variety, year<br>
color_wine: The color type of the wine<br>
Prices: Price of the wine USD<br>
ML: Bottle capacity in milliliters<br>
Rating: Verified consumer ratings out of 5<br>
Ratingsnum: The number of ratings<br>
Countrys: Country and region of production<br>
ABV: Alcohol by volume (ABV) content<br>
Rates: Simply lists the top wine experts who have reviewed the wine<br>

**[Vivino 1 dataset](https://www.kaggle.com/datasets/budnyak/wine-rating-and-price)**:<br>
**Scrapped:** 02/11/2023<br>
Name: Name of wine and year<br>
Country: Country of production<br>
Region: <br>
Winery: <br>
Rating: <br>
NumberOfRatings: <br>
Price: <br>
Year: <br>
category: <br>

**[Vivino 2 dataset](https://www.kaggle.com/datasets/joshuakalobbowles/vivino-wine-data)**:<br>
**Scrapped:** 01/02/2022<br>

**[Validation Dataset - Unknown Source Wines Without Review](https://www.kaggle.com/datasets/elvinrustam/wine-dataset)**
**Date uploaded:** 01/01/2024<br>
Title: The name or title of the wine.<br>
Description: A brief textual description providing additional details about the wine.<br>
Price: The cost of the wine in GBP.<br>
Capacity: The volume or size of the wine bottle.<br>
Grape: The primary grape variety used in making the wine.<br>
Secondary Grape Varieties: Additional grape varieties used in the wine blend.<br>
Closure: The type of closure used for the bottle.<br>
Country: The country where the wine is produced.<br>
Unit:<br>
Characteristics: The "Characteristics" feature encapsulates the unique and discernible flavors and aromas present in a particular wine.<br>
Per bottle / case / each: The quantity of wine included per unit (bottle, case, or each) sold.<br>
Type: The general category of the wine.<br>
ABV: The percentage of alcohol content in the wine.<br>
Region: The geographic region where the grapes used to make the wine are grown.<br>
Style: This feature describes the overall sensory experience and characteristics of the wine.<br>
Vintage: The year the grapes used to make the wine were harvested.<br>
Appellation: A legally defined and protected geographical indication used to identify where the grapes for a wine were grown.<br>

### 2. Data Preparation
- Clean all individual data files, assuring columns between all files align.<br>
- Include a column for rating source (vivino or wine.com)<br>
- Sensibly handle missing values/outliers.<br>
- Feature Engineering Ideas: <br>
        - Climate effects (with a combination of year and region info)<br>
        - Price-to-rating ratio<br>
        - Critic Name and Critic score interaciton variable.<br>
        - Binary was reviewed by critic X.<br>
- Scale features for unbiased model training.<br>
- Idenfity grape variety for every observation.<br>
- Create and include a measure for estimated drinking window.<br>
        - Certain grapes mature at different rates.<br>
        - Vintage Quality: Good vintages with optimal growing conditions can produce wines with greater aging potential.<br>
        - 
- Combine data sources ensuring that all duplicate values found, compared and datasets are combines without duplication. <br>

### 3. EDA - Aggregate Level
- **Interesting renowned regions to look at in particular:** Napa Valley (US), Piedmont and Tuscany (Italy), Bordeaux, Burgundy, Champagne and Rhone (France), <br>
- Plot scatter plot of wine ratings and prices to identify high rating low price (by region or vintage perhaps). <br>
- Explore correlations between prices and features (vintage, region, producer, grape variety, ratings).<br>
- Find initial coefficients with simple Linear Regresssion.<br>
- Investigate France regions in particular detail, it is said that "Burgundy is overpriced vs. Bordeaux which is underpriced".<br>
- Analyse score distributions and differences between wine.com and vivino distributions. <br>
- Identify wines producers which have averaged high critic scores over 3-4 vintages in a row. Could these be producers of interest.<br>
- Isolate limited production wines and analyse them seperately are there any in renowned regions that are below average prices for the region?<br> 
- **Idenfity up-and-coming / undervalued producers:** <br>
        - Look for wines with a positive differential between vintage/region average and wine price. Which migth suggest the wine maker is performing above the vintage standard, capable of producing a good wine in a bad vintage or an excellent wine in a good vintage.<br>
        - Identify producers with ratings on an upwards trajectory.<br>
        - How else might future winners or up-and-coming producers be identified? <br>
- Interesting idea to explore - price distribution of producers, clustering and interaction variable with rating :<br>
        - Question: Is a 5-star rating of a wine from an 'high-end' producer worth more than a 5-star rating of a mass market producer? Are more expensive wines held to higher standards or are they just better overall therefore recieve generally higher ratings? 
        - Make a table of producers with average prices. <br>
        - Cluster / group the producers, in a high-end vs mass-market kind of split.<br>
        - Make an interaction variable between rating and producer cluster. Pehaps this could capture high rating * high end producer = very expensive wine or low rating * high-end producer = unusually cheap wine for producer type.<br>

### 4. Unsupervised Learning - Clustering: <br>
- Use clustering methods to group wines based on region, year, rating and grape variety.<br>
- Analyse clusters and split clusters into high/low quality based on ratings.<br>
- Plot individual clusters with price included.<br>

### 5. Regression Modelling
- Discover predictive features of price with white box regression modelling. Linear regression to analyse the linear relationship between features and price appreciation. Decision Trees to identify important features and potential non-linear relationships.<br>
- Use black box modelling methods to maximise for model accuracy, random forests, XGBoost, somehighly unnecessary and costly neural network! :D<br>
- If a model with high accuracy is created perhaps our application and include within it some measure of how over/underpriced when a bottle of wine is entered.<br>
- Target: wine price.<br>

#### Other Modelling Ideas 
- Test different models on different segments of the wine market. Do certain models suit certain market segments? Would it be wise to seperate the models in that sense? If region == X use model Y? <br>

### 6. Evaluation and Iteration
- Use metrics like root mean squared error (RMSE) or R-squared to assess prediction accuracy.<br>
- Train our production model on the full avaliable training dataset. Create some predictions of price on a random selection of wines in the validation_dataset.csv.<br> 
- validation_dataset.csv is a recent scrape from Vivino of circa 1000 wines which will provide a test of the robustness of our model on unseen and more recent data.<br>

## Potential Challenges
- Lack of important and useful attributes to predict wine prices. Prestige of <br>
- Computational and resource limitations for advanced models.<br>
- Risk of models predicting current trends without offering new insights.<br>

## The Application: 
Purpose: Allow wine consumers to better understand their choices of wine, compare their selection to back vintages both in quality and price and get some sense of the value of the wine they are researching. <br>

**Functionality:**
1. Type in the name of a wine and see how back vintages have performed in ratings and prices. <br>
2. Recommend similar wines to try. <br>
3. Say if the wine they are researching is overpriced, underpriced or just right. <br>

## Future Analysis Ideas: 
        * 
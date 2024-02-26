# Wine Wine Wine - README 
Capstone Aaran Daniel
Predictive Modelling and Application Development for Consumer Wines

## Intro
This isn't the first wine-based Data Science project and it wont be the last. Hopefully this one can put a fresh spin on an industy subject to the interest of many a data-scientist. 

In this project several data scrapes from multiple source 


## Problem Statement


## Primary Aim
Using historical price data of wines develop a predictive model for prices and help consumers identify bargain wines.  

## Secondary Aims
- Identify key price predictive features.
- Identify price/rating predictive power of certain renowned reviewers - compare this to consumer ratings 
- Identify undervalued wines which match features of higher value wines but at a bargain price. 
- Identify region/vintages that are highly rated compared to others. 
- Identify producers 
- Build an application which allows win buyers to search a wines and returns recommended similar wines, previous vintage price/ratings and an estimate of drinking window.

## Metric for Success
Model that is able to predict prices to within 5% of actual price.<br>

## Original Datasets: 
**[Wine.com dataset](https://www.kaggle.com/datasets/salohiddindev/wine-dataset-scraping-from-wine-com):**
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



**[Validation Dataset - Unknown Source Wines Without Review](https://www.kaggle.com/datasets/elvinrustam/wine-dataset)**
**Date uploaded:** 01/01/2024<br>
Title: The name or title of the wine.<br>
Description: A brief textual description providing additional details about the wine.<br>
Price: The cost of the wine.<br>
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

## Cleaned and Combined Dataset: 


## Process

### 1. Data Collection
- **Source**: Vivino.come and wine.com scrapes obtained via Kaggle<br>
- **Key Features**:price, vintage, region, producer, critics ratings, consumer ratings, grapes variety, rarity / production quantity, brand power, Wine-Searcher rank / Google reach.<br>


### 2. Data Preparation
- Combine data sources, handle missing values/outliers.<br>
- Feature Engineering: <br>
        - Climate effects (with a combination of year and region info)<br>
        - Price-to-rating ratio<br>
        - Critic Name and Critic score interaciton variable.<br>
        - Binary was reviewed by critic X.<br>
- Scale features for unbiased model training.<br>
- Are critics ratings more/less predictive of prices within certain regions that are more under the spotlight?<br>

### 3. EDA - Aggregate Level
- Interesting renowned regions to look at in particular: Napa Valley in the US, Piedmont and Tuscany in Italy, and then Bordeaux, Burgundy, Champagne and Rhone in France.<br>
- Plot scatter plot of wine ratings and prices to identify high rating low price (by region perhaps). <br>
- Explore correlations between prices and features (vintage, region, grape variety, critic ratings).<br>
- Find initial coefficients with simple Linear Regresssion.<br>
- Investigate is "Burgundy is overpriced at the moment vs. Bordeaux which is underpriced".<br>
- Analyse score distributions, and critics score distributions. <br>
- Identify wines producers which have averaged high critic scores over 3-4 vintages in a row. Could these be producers of interest.<br>
- Isolate limited production wines and analyse them seperately are there any in renowned regions that are below average prices for the region?<br> 
- **Idenfity up-and-coming / undervalued producers:** <br>
        - Look for wines with a positive differential between vintage/region average and wine price. Which migth suggest the wine maker is performing above the vintage standard, capable of producing a good wine in a bad vintage or an excellent wine in a good vintage.<br>
        - Identify producers with ratings on an upwards trajectory.<br>
        - How else might future winners or up-and-coming producers be identified? <br>
- **Unsupervised learning / Clustering:** <br>
Aim: Create a short list of wines to focus on for time series modeling (step 3).<br>
Method: Unsupervised learning, hide price from the model then cluster the wines. Plot the individual clusters with price added back in, identify clusters where ceratin wines are underpriced (or overpriced) compared to the rest of the cluster.<br>
Granularity: Same as step 1, at the wine level with prices aggregated over time in someway.<br>

### 5. Regression Modelling

**STEP ONE - REGRESSION**
Aim: Discover more predictive features which should be used as exogenous variables in time series modelling (step 3)<br>
Method: White box regression modelling. Linear regression to analyse the linear relationship between features and price appreciation. Decision Trees to identify important features and potential non-linear relationships.<br>
Granularity: At the wine level, where each observation is a different wine, with price over time aggregated (see target below).<br>
Potential Targets: 1. Average price over timeframe or;2. Current market price?; <br>

#### Other Modelling Ideas 


### 6. Evaluation and Iteration
- Use metrics like root mean squared error (RMSE) or R-squared to assess prediction accuracy.<br>

## Potential Challenges
- Insufficient data or attributes.<br>
- Lack of domain knowledge for market segmentation.<br>
- Time series modelling difficulties and unpredictability. <br>
- Possible need for bespoke models per wine category.<br>
- Computational and resource limitations for advanced models.<br>
- Risk of models predicting current trends without offering new insights.<br>

## The Application: 
Purpose: Allow sales are marketing team to quickly search wines and provide historical returns information to prospective customers (potential wine investors). 

**Functionality:**
1. Type in the name of a wine and see how back vintages have performed over different time horizons (i.e. how they have appreciated). 
2. Recommend a portfolio based on a budget (e.g. these are the most undervalued wines on the market right now).

## Future Analysis Ideas: 
        * Consider NLP approach, incorporating sentiment analysis from wine reviews. Can we gain an edge on the market by scraping sentiment from vivino, twitter, reddit for sentiments on vintage wines. 
        * Setting some predictions on wines / categories or interest and waiting. In 3 or 4 months down the line seeing how the model performs. The more we do this the better.
        * Influencer analysis or scraping En Primeur releases, Decanter World Wine Awards or International Wine Challenge, to get an edge on the market. 
        * Explore additional regions: Priorat in Spain, Willamette Valley in Oregon, or Stellenbosch in South Africa.
        * Look for consistent winners in prestigious awards like 


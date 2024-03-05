# README - Why, Why, Wine
**Price Predictive Modelling of Consumer Wines an Application for Wine Comparison**<br>
Capstone Project by Aaran Daniel<br>

How important is region, vintage and rating to the price of a wine? 



## Intro:<br>
This project puts a fresh twist on a topic that is the interest of many a thirsty Data Scientist, wine. Over 50,000 wines are analysed in a project designed to shed light on what dictates the prices of consumer wine and help drinkers identify some delicious bargains. By combining datasets from two different websites, three seperate scrapes, it is hoped that deficiencies in any single datasource are mitigated, allowing for the creation of a price predictive model more robust to unseen data.<br> 

When identifying undervalued wines this project delves deeper than a basic comparison of rating and price (i.e. those wines with a higher than average rating and a lower than average price are designated undervalued). The question is asked, do consumers rate wines price contextually ("good for its price") or based on inherent quality/experience of the wine ("good or bad regardless of price")<br> 

The end result will be a high-acccuracy price predictive model and an application designed for users to input wines and receive similar wines, vintage comparisons and some measure of value-for-money. Helping the user decide if the wine they are interested in is overvalued, undervalued or just-right. Some revealing price predictive features and interesting insights sprinkled in along the way.<br> 

## Problem Statement:<br>
- Too many wines out on the market how can a user know if they are getting good value for money or how the wine in their hand compares to previous vintages or wines from the same region?<br>
- We look to understand what features are most predictive of wine prices and in doing so identify oppotiunities to purchase great wines at bargain prices.<br>

## Primary Aim:<br>
Using historical price data of wines develop a predictive model for prices and help consumers identify bargain wines.<br>

## Secondary Aims:<br>
- Investigate the relationship between price and rating. Do consumers take into account the price before rating a wine or are all ratings equal?<br>
- Identify key price predictive features.<br>
- Investigate if a renowned reviewer having reviewed a wine is predictive for prices.<br>
- Find undervalued wines which match features of higher value wines but at a discount price tag.<br>
- Identify region/vintages that are highly rated compared to others. <br>
- Suggest up-and-coming wines or producers that appear to be gaining in reputation and/or price.<br>
- **Build an application** which allows wine buyers to search a wines and returns recommended similar wines, previous vintage price/performance and an estimate of ideal drinking window.<br>

## Metric for Success<br>
- A model that is able of predicting prices to within 5% of actual price.<br>
- Functioning application that is able to take as input even wines not in the dataset.<br>

## Cleaned and Combined Dataset Data Dictionary:<br>
| Column Name | Data Type | File | Description |
|---|---|---|---|
| name | object | cleaned_combined.csv | The name of the wine, often formulated <winery><grape><vintage> |
| country | object | cleaned_combined.csv | Origin country of wine, USA as 'United States', UK countries seperate e.g. 'England' |
| region | object | cleaned_combined.csv | Region in which the wine was produced, for the U.S. this is states |
| vintage | object | cleaned_combined.csv | Year the grapes were picked otherwise known as vintage |
| producer | object | cleaned_combined.csv | A two word code for producer names | 
| rating | | cleaned_combined.csv |
| rating_qty | | cleaned_combined.csv |
| price | float |cleaned_combined.csv | Price in GBP for 750ml single bottle of wine |
| grape_variety | object | cleaned_combined.csv | 
| wine_variety | object | cleaned_combined.csv | Categorical variable representing wine type (red, white, sparkling, rose, unknown) |
| abv | float | cleaned_combined.csv | 
| reviewed_by | object | cleaned_combined.csv | Initials representing certain renowned reviewers for full reviewer names [follow this link](https://www.wine.com/content/landing/icons-explained#:~:text=Professional%20Ratings,range%20within%20the%20tasting%20note) |
| from_vivino | boolean | cleaned_combined.csv | True is data originates from vivino false if data from wine.com |



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
**Scrapped:** 22/02/2020<br>
Name: Name of wine and year<br>
Price: price of bottle in EUR €<br>


**[Vivino 2 dataset](https://www.kaggle.com/datasets/joshuakalobbowles/vivino-wine-data)**:<br>
**Scrapped:** 01/02/2022<br>
Price: price of bottle in EUR €

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
- Include a column for source (vivino or wine.com)<br>
- Sensibly handle missing values/outliers.<br>
- Feature Engineering Ideas: <br>
        - Climate effects (with a combination of year and region info)<br>
        - Price-to-rating ratio<br>
        - Critic Name and rating interaciton variable.<br>
        - Binary was reviewed by critic X.<br>
- Idenfity grape variety for every observation.<br>
- Create and include a measure for estimated drinking window.<br>
        - Certain grapes mature at different rates.<br>
        - Vintage Quality: Good vintages with optimal growing conditions can produce wines with greater aging potential.<br>
- Combine data sources ensuring that all duplicate values found, compared and datasets are combines without duplication. <br>

### 3. EDA - Aggregate Level
- Explore correlations between prices and features (vintage, region, producer, grape variety, ratings).<br>
- Investigate specifically correlation between wine prices and their ratings.<br>
- Plot scatter plot of wine ratings and prices to identify high rating low price (by region or vintage perhaps). <br>
- Analyse score distributions and differences between wine.com and vivino distributions. <br>
- Identify wines producers which have averaged high critic scores over 3-4 vintages in a row. Could these be producers of interest.<br>
- Isolate limited production wines and analyse them seperately are there any in renowned regions that are below average prices for the region?<br> 
- **Interesting renowned regions to look at in particular:** Napa Valley (US), Piedmont and Tuscany (Italy), Bordeaux, Burgundy, Champagne and Rhone (France), <br>
- Investigate France regions in particular detail, it is said that "Burgundy is overpriced vs. Bordeaux which is underpriced".<br>
- **Idenfity up-and-coming / undervalued producers:** <br>
        - Look for wines with a positive differential between vintage/region average and wine price. Which might suggest the wine maker is performing above the vintage standard - therefore capable of producing a good wine in a bad vintage or an excellent wine in a good vintage.<br>
        - Identify producers with ratings on an upwards trajectory.<br>
        - How else might future winners or up-and-coming producers be identified? <br>
- **Identifying undervalued wines:**
        - Rating Distribution Analysis by Price Segments: Segment wines by price brackets and analyze the distribution of their ratings.<br>
- Isolate wines of above a certain price bracket and perform some seperate analysis of this group in particular.<br>

### 4. Unsupervised Learning - Clustering: <br>
- Use clustering methods to group wines based on region, year, rating and grape variety.<br>
- Analyse clusters and split clusters into high/low quality based on ratings.<br>
- Plot individual clusters with price included.<br>
- **Interesting idea to explore - price distribution of producers, clustering and interaction variable with rating:**<br>
        - Question: Is a 5-star rating of a wine from an 'high-end' producer worth more than a 5-star rating of a mass market producer? Are more expensive wines held to higher standards or are they just better overall therefore recieve generally higher ratings?<br>
        - Make a table of producers with average prices. <br>
        - Cluster the producers, in a high-end vs mass-market kind of split.<br>
        - Make an interaction variable between rating and producer cluster. Pehaps this could capture, for example,  high rating * high-end producer = super expensive wine, in the regression modelling phase.<br>

### 5. Regression Modelling
- One hot encode categorical variables. <br>
- Target: wine price.<br>
- Find initial coefficients with simple Linear Regresssion.<br>
- Scale features for unbiased model training.<br>
- Discover predictive features of price with white box regression modelling. Linear regression to analyse the linear relationship between features and price appreciation. Decision Trees to identify important features and potential non-linear relationships.<br>
- Consider distribution of variables and making logarithmic transformations of target or features.<br>
- Use black box modelling methods to maximise for model accuracy, random forests, XGBoost, perhaps even some highly unnecessary and costly neural network! ;) <br>
- If a model with high accuracy is created, perhaps our application can include within it some measure of how over/underpriced when a bottle of wine is entered?<br>

#### Other Modelling Ideas 
- Test different models on different segments of the wine market. Do certain models suit certain market segments? Would it be wise to seperate the models in that sense? If region == X use model Y? Is this possible? <br>
- Conduct regression using only ratings alone as a feature, compare the models' performance to the previous regression model. This could help address the question of whether price confounds ratings?<br>
- [Study reference](https://digitalcommons.kennesaw.edu/cgi/viewcontent.cgi?referer=&httpsredir=1&article=1017&context=amj) "Our findings indicate that for low wine ratings, consumers rely more on the price-perceived quality heuristics. This implies... sellers may need to raise the price to increase perceptive quality. However for wine with high ratings, consumers rely more on the wine information. Hence wine labels or literature needs to have more information
available to support the high ratings."<br>

### 6. Evaluation and Iteration
- Use metrics like root mean squared error (RMSE) or R-squared to assess prediction accuracy.<br>
- Train our production model on the full avaliable training dataset. Create some predictions of price on wines in the validation_dataset.csv.<br> 
- validation_dataset.csv is a recent scrape from Vivino of circa 1000 wines which will provide a test of the robustness of our model on unseen and more recent data.<br>

## Potential Challenges
- Lack of important and useful attributes to predict wine prices. <br>
- Data Quality and Completeness: The project relies on data from multiple sources, which may have inconsistencies, missing values, or errors.<br>
- Estimating the drinking window of wines based on grape variety and vintage quality could prove difficult without just using second hand information from reasearch. <br>
- Scalability of the Application: making an application which allows any wines to be inputted and remains up-to-date with the latest wine data could be challenging. <br>

## The Application: 
Purpose: Allow wine consumers to better understand their choices of wine, compare their selection to back vintages both in quality and price and get some sense of the value of the wine they are researching. <br>

**Functionality:**
1. Type in the name of a wine and see how back vintages have performed in ratings and prices. <br>
2. Recommend similar wines to try. <br>
3. Say if the wine they are researching is overpriced, underpriced or just right. <br>

## Future Analysis Ideas: 
        * Review Text Analysis: Apply natural language processing (NLP) to analyze review texts for mentions of price or value. Determine if reviews often justify ratings with price (e.g., "great for the price") versus focusing solely on taste or experience. Or how frequently 'price' is mentioned in wine ratings across different platforms. A higher frequency of price mentions in positive (or negative) ratings could indicate a price-contextual evaluation.


## Things to revisit: 
1. Group the producers more. 
2. More methods to extract or find grape varietry for viv_1

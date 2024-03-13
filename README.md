# README - What, Where and Wine 
**Price Predictive Modelling and Application for Consumer Wines**<br>
Aaran Daniel<br>

## Executive Summary:<br>
This project puts a fresh twist on a topic that is the interest of many a thirsty Data Scientist, wine. Over 50,000 wines are analysed in a analysis designed to shed light on what dictates the prices of consumer wine and help drinkers identify some delicious bargains. Combining datasets from two different websites, three seperate scrapes, it is hoped that the creation of a price predictive model more robust to unseen data is facilitated.<br> 

When identifying undervalued wines this project delves deeper than a basic comparison of rating and price. The end result will be a high-acccuracy price predictive model and an application designed, our very own digital sommerlier Casi. Casi comes in two parts: 1. A game of guess the wine price; 2. A wine valiation tool, helping a user decide if the wine they are interested in is priced sensibly. Some revealing price predictive features and interesting insights are sprinkled in along the way.<br> 

A limitaiton of this project is that wine prices differ countries for many reasons such as taxes and transportation costs. The data also varies in age and therefore some prices might be slightly out dated. Lastly the valuation ability of our app is limited to the regions, producers and countries upon which the model was trained. <br> 

## Problem Statement:<br>
Too many wines out on the market how can a user know if they are getting good value for money? How the wine in their hand compares to previous vintages or wines from the same region. This project looks to understand what features are most predictive of wine prices and in doing so identify opportunities to purchase great wines at bargain prices.<br>

## Primary Aim:<br>
Using historical price data of wines develop a predictive model for prices and help consumers identify bargain wines.<br>

## Secondary Aims:<br>
- Investigate the relationship between price and rating. Do consumers take into account the price before rating a wine or are all ratings equal?<br>
- Identify key price predictive features.<br>
- How important is region, vintage, producer and rating to the price of a wine? <br>
- Find undervalued wines which match features of higher value wines but at a discount price tag.<br>
- Identify region/vintages that are highly rated compared to others. <br>
- **Build an application** which allows wine buyers to have fun, learn about wines and value bottles.<br>

## Metric for Success:<br>
- A model that is able of predicting prices to within 5% of actual price.<br>
- Functioning application MVP providing a base which can be built upon in future.<br>

## Cleaned and Combined Dataset Data Dictionary:<br>
| Column Name | Data Type | File | Description |
|---|---|---|---|
| name | object | cleaned_combined.csv | The name of the wine, often formulated <name><winery><grape><vintage> or just <winery><grape><vintage> |
| country | object | cleaned_combined.csv | Origin country of wine, USA as 'United States', UK countries seperate e.g. 'England' |
| region | object | cleaned_combined.csv | Region in which the wine was produced, for the U.S. this is states |
| vintage | object | cleaned_combined.csv | Year the grapes were picked otherwise known as vintage |
| producer | object | cleaned_combined.csv | A two word code for producer names | 
| rating | | cleaned_combined.csv |
| rating_qty | | cleaned_combined.csv |
| price | float |cleaned_combined.csv | Price in USD for 750ml single bottle of wine |
| grape_variety | object | cleaned_combined.csv | 
| wine_variety | object | cleaned_combined.csv | Categorical variable representing wine type (red, white, sparkling, rose, unknown) |
| abv | float | cleaned_combined.csv | 
| reviewed_by | object | cleaned_combined.csv | Initials representing certain renowned reviewers for full reviewer names [follow this link](https://www.wine.com/content/landing/icons-explained#:~:text=Professional%20Ratings,range%20within%20the%20tasting%20note) |
| from_vivino | boolean | cleaned_combined.csv | True is data originates from vivino false if data from wine.com |



## Process

### 1. Data Collection<br>
- **[Wine.com dataset](https://www.kaggle.com/datasets/salohiddindev/wine-dataset-scraping-from-wine-com):**<br>
**Date uploaded:**  02/11/23<br>

**[Vivino 1 dataset](https://www.kaggle.com/datasets/budnyak/wine-rating-and-price)**:<br>
**Date uploaded:**  22/02/2020<br>

**[Vivino 2 dataset](https://www.kaggle.com/datasets/joshuakalobbowles/vivino-wine-data)**:<br>
**Date uploaded:**  01/02/2022<br>

**[Vivino 3 dataset](https://www.kaggle.com/datasets/nikitatkachenko/vivinoredwine/data)**<br>
**Date uploaded:** 10/03/2024<br>

### 2. Data Preparation
- Clean all individual data files, assuring columns between all files align.<br>
- Include a column for source (vivino or wine.com) to keep track of data source.<br>
- Sensibly handle missing values/outliers.<br>
- Feature Engineering Ideas: <br>
        - Climate effects (with a combination of year and region info), was tried but did not improve model predictiveness.<br>
        - Price-to-rating ratio - for EDA.<br>
        - Binary was reviewed by critic X.<br>
        - Log transformation and polynomials.<br>
- Idenfity grape variety for every observation.<br>
- Idenfity wine variety for every observation and only include red, white, rose and sparkling (non-fortified) wines.<br>
- Idenfity and isolate producer (winery) for every observation.<br>
- Combine data sources ensuring that all duplicate values found, compared and datasets are combines without duplication.<br>

### 3. EDA - Aggregate Level
- Explore correlations between prices and features (vintage, region, producer, grape variety, ratings).<br>
- Investigate specifically correlation between wine prices and their ratings.<br>
- Plot scatter plot of wine ratings and prices to identify high rating low price (by region and vintage). <br>
- Identify wines producers which have price/rating ratios more affordable than the region vintage average, 3-4 vintages in a row.<br>
- **Idenfity up-and-coming / undervalued producers:** <br>
        - Look for wines with a positive differential between vintage/region average and wine price. Which might suggest the wine maker is performing above the vintage standard - therefore capable of producing a good wine in a bad vintage or an excellent wine in a good vintage.<br>
        - Identify producers with ratings on an upwards trajectory.<br>
- **Identifying undervalued wines:**
        - Plot rating and price by country or region and isolate wines with abnormally low prices/high ratings. <br>

### 4. Regression Modelling
- Label encooding was decided upon as opposed to binary encoding due to the quantity of categorical featyres. <br>
- Target: log wine price used as more normally distributed and improved model predictiveness.<br>
- Found initial baseline more and coefficients with simple Linear Regresssion.<br>
- Scaled features for unbiased model training but it did not significantly affect model performance.<br>
- Decision Tree models proved to be most accurate which is to be expcted with a high number of important categorical features and non-linear relationships (label encoded producer names for example).<br>
- Random forests gave us the most accurate model in terms of R2 and RSME. <br>
- All models were hyper parameter tuned. <br>
- SHAP values, feature importance and recursive feature elimation done, finding region, country, vintage, producer and rating were the most predictive features. <br>

### 5. Model Validation
- 10% of the original data set was kept completely seperate from the model creation phase to test production model(s). <br>
- Best Decision Tree model R2 of 0.862, price RSME of $1.36. <br>
- Best Random Forests model R2 of 0.924, price RSME of $1.26. <br>

### 6. The Application
Purpose: Educate wine consumers and allow them to better understand their choices of wine, compare their selection to back vintages both in quality and price and get some sense of the value of the wine they are researching. Application was split into two parts:
1. An educational game where you attempt to beat Casi our price predicting sommelier;<br>
2. A valuation feature where casi will value any wine for you based on the informaiton you input!<br>

## Conclusions & Findings:



## Future Analysis Ideas - Further Investigation: 
        * Review Text Analysis: Apply natural language processing (NLP) to analyze review texts for mentions of price or value. Determine if reviews often justify ratings with price (e.g., "great for the price") versus focusing solely on taste or experience. Or how frequently 'price' is mentioned in wine ratings across different platforms. A higher frequency of price mentions in positive (or negative) ratings could indicate a price-contextual evaluation.
        * Prices of wines for various reasons differ between countries, those scrapes done in EUR will be price differently to those done in GBP or USD. Taxes are different, import taxes are different and websites might deal with price conversions differently. 
        * Investigate if a renowned reviewer having reviewed a wine is predictive for prices.
        * Seperate out fine wines and create and include a measure for estimated drinking window. Certain grapes mature at different rates. Vintage Quality: Good vintages with optimal growing conditions can produce wines with greater aging potential.
        * Test different models on different segments of the wine market. Do certain models suit certain market segments? Would it be wise to seperate the models in that sense? If region == X use model Y? Is this possible? 
        Conduct regression using only ratings alone as a feature, compare the models' performance to the previous regression model. This could help address the question of whether price confounds ratings?
        Study reference](https://digitalcommons.kennesaw.edu/cgi/viewcontent.cgi?referer=&httpsredir=1&article=1017&context=amj) "Our findings indicate that for low wine ratings, consumers rely more on the price-perceived quality heuristics. This implies... sellers may need to raise the price to increase perceptive quality. However for wine with high ratings, consumers rely more on the wine information. Hence wine labels or literature needs to have more information available to support the high ratings."<br>
        * Calculate an estimating the drinking window for fine winesbased on grape variety and vintage quality. <br>

## Areas for Improvement:
1. Group the producers more thoroughly.
2. Review methods to extract or find grape varietry for vivino 1 dataset.
3. Do exact same eda and modelling for higher price wines. What is the difference? It is generally said minimum for IG wines is $100.
4. Predict ratings using price and other features. Try predicting ratings without price using RNNs perhaps. 
5. Build a classification model that classifies wines as over/underpriced.
6. Develop the application game to have difficulty levels and to be more aesthetically pleasing. 
7. Further investigation into specific underpriced wines. 
8. Make an application which allows any wines to be inputted - it proved difficult to find a free API for wine information. 


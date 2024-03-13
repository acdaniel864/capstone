
# code taken from Matt Brems 
def compare_histograms(imputed_column, original_column, x_label, y_label = 'Frequency', bins = 30):
    import matplotlib.pyplot as plt
    import numpy as np
    import statistics
    """
    Compares two histograms: one for the original data column and one for the imputed data column.
    This function plots two histograms vertically to visually compare the distribution of the original
    and imputed data. It also marks the mean values of both distributions on the histograms for easier comparison.

    Parameters:
    - imputed_column (array-like): The column of data that has been imputed.
    - original_column (array-like): The original column of data before imputation.
    - x_label (str): The label for the x-axis, which describes the data being histogrammed.
    - y_label (str, optional): The label for the y-axis, which defaults to 'Frequency'. This describes
      the count of data points within each bin of the histogram.

    Outputs multiple histogram plots. 
    """
    fig, (ax0, ax1) = plt.subplots(nrows = 2, ncols = 1, figsize = (16,9))

    # Set axes of histograms.
    mode = statistics.mode(imputed_column)
    rnge = max(original_column) - min(original_column)
    xmin = min(original_column) - 0.02 * rnge
    xmax = max(original_column) + 0.02 * rnge
    #ymax = 100
    try:
        ax0.set_xlim(xmin, xmax)
        ax1.set_xlim(xmin, xmax)
    except: 
        ax0.set_xlim(0, 20)
        ax1.set_xlim(0, 20)

    # Set top labels.
    ax0.set_title('Real Histogram', position = (0,1), ha = 'left', fontsize = 25)
    ax0.set_xlabel(x_label, position = (0,0), ha = 'left', fontsize = 25, color = 'grey', alpha = 0.85)
    ax0.set_ylabel(y_label, position = (0,1), ha = 'right', va = 'top', fontsize = 25, rotation = 0, color = 'grey', alpha = 0.85)
    ax0.set_xticks([])
    ax0.set_yticks([])

    # Generate top histogram.
    ax0.hist(original_column, bins = bins, color = '#185fad', alpha = 0.75, label = '')
    ax0.axvline(np.mean(original_column), color = '#185fad', lw = 5, label = 'True Mean')
    ax0.legend(prop={'size': 15}, loc = 1)

    # Set bottom labels.
    ax1.set_title('Imputed Histogram', position = (0,1), ha = 'left', fontsize = 25)
    ax1.set_xlabel(x_label, position = (0,0), ha = 'left', fontsize = 25, color = 'grey', alpha = 0.85)
    ax1.set_ylabel(y_label, position = (0,1), ha = 'right', va = 'top', fontsize = 25, rotation = 0, color = 'grey', alpha = 0.85)
    ax1.set_xticks([])
    ax1.set_yticks([])
    
    # Generate bottom histogram.
    ax1.hist(imputed_column, bins = bins, color = 'orange', alpha = 0.75, label = '', stacked = True)
    ax1.axvline(np.mean(original_column), color = '#185fad', lw = 5, label = 'True Mean')
    ax1.axvline(np.mean(imputed_column), color = 'darkorange', lw = 5, label = 'Imputed Mean')
    ax1.legend(prop={'size': 15}, loc = 1)

    plt.tight_layout();


def compare_close_vintages_in_a_country(df, country, vintage, show_country = False):
    import matplotlib.pyplot as plt
    import numpy as np

    country_df = df[df['country'] == country]
    
    # Check there are at least 3 vintages in the country
    vintage_counts = country_df.groupby('vintage').filter(lambda x: len(x) >= 3)
    
    # Calculate average rating and price by vintage.
    avg_metrics_by_vintage = vintage_counts.groupby('vintage')[['rating', 'price']].median().reset_index()
    
    avg_metrics_by_vintage['rating'] = avg_metrics_by_vintage['rating'].round(2)
    avg_metrics_by_vintage['price'] = avg_metrics_by_vintage['price'].round(2)
    
    vintage_position = avg_metrics_by_vintage[avg_metrics_by_vintage['vintage'] == vintage].index
    
    if not vintage_position.empty:
        position = vintage_position[0]
        
        # Find start and end positions for the vintage.
        start_pos = max(0, position - 3)
        end_pos = min(len(avg_metrics_by_vintage), position + 4)
        
        # Choose closest 6
        closest_vintages = avg_metrics_by_vintage.iloc[start_pos:end_pos].copy()
        if show_country == True:
          closest_vintages['Country'] = country 
        closest_vintages.rename(columns={'vintage': 'Vintage', 
                                         'rating' : 'Avg Rating', 'price' : 'Avg Price'}, inplace = True)
        closest_vintages['Vintage'] = closest_vintages['Vintage'].astype(str)
        return closest_vintages
    else:
        print("We don't have enough data for vintage comparison on this occasion.")

def plot_country_vintage_comparison(df, vintage, location = None, plot_region = False, rateymin = 2.5, pricexmax = 100):
    import matplotlib.pyplot as plt
    import numpy as np
    # used chat gpt to help with this graph because it got pretty complicado
    if location == None:
        location_data = df

    else:
        if plot_region == True: 
            location_data = df[df['region'] == location]

        else:
            location_data = df[df['country'] == location]

    
    avg_metrics = location_data.groupby('vintage')[['rating', 'price']].median().reset_index()
    
    fig, ax1 = plt.subplots(figsize=(10, 5))

    colour1 = '#FFBF00'
    ax1.set_xlabel('Vintage')
    ax1.set_ylabel('Rating', color=colour1)
    ax1.set_xlim(2004.5,2021.5)
    ax1.set_ylim(rateymin,5)
    ax1.scatter(avg_metrics['vintage'], avg_metrics['rating'], color=colour1, label='Average Rating')
    ax1.tick_params(axis='y', labelcolor=colour1)
    
    # Change apperance of selected vintage
    specific_vintage_rating = avg_metrics[avg_metrics['vintage'] == vintage]['rating']
    ax1.scatter(vintage, specific_vintage_rating, color='darkblue', s=100, label=f'Rating in {vintage}', edgecolors='black')
    
    ax2 = ax1.twinx()
    colour = '#9437FF'
    ax2.set_ylim(0,pricexmax)
    ax2.set_ylabel('Average Price', color=colour)
    ax2.bar(avg_metrics['vintage'], avg_metrics['price'], color=colour, label='Average Price', alpha=0.6)
    ax2.tick_params(axis='y', labelcolor=colour)

    # Adjust x-axis to show marker every 2 years

    ax1.set_xticks(np.arange(2004, 2020 + 1, 2))
    
    
    # Title
    ax1.set_title(f'Comparison of Avg. Rating & Price for Wines in {location} by Vintage')
    
    # Create a legend
    rating_legend = plt.Line2D([0], [0], marker='o', color='w', label='Average Rating', markerfacecolor= '#FFBF00')
    price_legend = plt.Line2D([0], [0], marker='s', color='w', label='Average Price',
                              markerfacecolor='#9437FF')
    specific_vintage_legend = plt.Line2D([0], [0], marker='o', color='w', label=f'Rating in {vintage}',
                                          markerfacecolor='darkblue', markeredgewidth=1.5, markeredgecolor='black')
    
    ax2.legend(handles=[rating_legend, price_legend, specific_vintage_legend], loc='upper left')
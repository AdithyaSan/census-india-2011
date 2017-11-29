# census-india-2011

# GOAL: Using Indian Census Data from 2011 to answer the given questions
1.	Create a geographic map of states with low literacy rates.
2.	Find out most similar districts in Bihar and Tamil Nadu. Similarity can be based on any of the columns from the data.
3.	How does the mobile penetration vary in regions (districts or states) with high or low agricultural workers?


# Data Cleaning:
There were no missing values in the dataset.
Only the names of certain states have been altered to match with the OLD NAMES.
(& ampersand) was changed to "AND"
	Example: Jammu & Kashmir - Jammu and Kashmir

# Importing required libraires:
	1. Pandas
	2. Numpy
	3. seaborn
	4. math
	5. itertools (groupby)
	6. matplotlib
	7. Basemap

# Detailed view of the data
The describe() method gives a detailed view of the data, where the min, max, mean and other metrics mentioned below can be observed. It gives an intuition as to what kind of data we are working with in our scenario.
The names of all columns in our dataset have been mentioned below.

# Number of states in the dataset:
35 (States and Union Territories)
One thing to be noted here is that Telangana state is not mentioned, as it was not formed as of 2011

# 1. Indian States with the least Literacy rate
For finding the literacy rate for each state, we calculated the literacy rate by dividing total literate population by total population. This has been stored in literacy_rate.
Also, since we are mainly interested in the states with lower literacy rates, we have also checked for those top 7 states with the least literacy compared to other ones.

Assumptions:
According to the definition of literacy rate on the official wikipedia page (please see: https://en.wikipedia.org/wiki/Literacy_in_India), it has been mentioned that literacy rate is calcuated for ages 7 and above, but in our dataset, we do not have a clear division as such. This is the reason why we simply considered the toal population as opposed to the actual population to be considered.

All the Union Territories of our country have been included in this, just to maintain uniformity among the data. There are 7 Union Territories and 28 states in total.

# 2. Similarities between districts in Bihar and Tamil Nadu
To find the similarity measure between the districts in Bihar and Tamil Nadu (TN), we have first created two dataframes for each state and dropped the district codes and state names - while only considering the District names and comparing their data.
As for the similairty measure - we have used the Cosine Similarity measure
The Cosine similarity measure is one of the similairty measuring techniques between two non-zero vectors and the angle between them. If the angle is 0 (cos0 = 1) then it indicates that they are similar to each other as opposed to the angle of 90 (which is cos90 = 1)

After finding the cosine similarities, we have plotted a heatmap to visualize the most similar districts and the ones that are not similar at all.

# 3. Mobile Penetration Rates and Agricultural Workers
For this case, we first got the separate data for households with mobile phones and the population of agricultural workers in different lists.
It was found out that UTTAR PRADESH was the state that had the "most number of households with mobile phones" and the most number of "agricultutal workers"

Assumptions:
The first assumption made is that 'households with mobile phones' and 'population of agricultutal workers' are two metrics that can be compared - because we do not have any strict confirmation that says that the households are in rural/urban areas, since most of the agricultural work is carried out in the rural parts of the state.
Union Territories have also been considered as states - however, in the end - we have chose to ignore those with 0 or very less agricultutal workers. For example, Lakshadweep has 0 agri workers but there are mobile users.

# Checking if we can discover factors that influence the literate population
To do this, we have first removed the District Code, District Name and Literate Education from the data, so that there is no data leakage with respect to the liteate population.

We made use of the Random Forest Regressor from the 'sklearn' package to implement a Random Forest Algorithm on the data while regressing on "Literate".

Even though the results determining the feature importance did not make much sense in the end, I believe that this is a good way to check what factors are most important in influencing the literate population in the country.

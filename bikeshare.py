#*********** Udacity Nanodegree program in Programming for Data Science using Python
#*********** Project: Explore US Bikeshare Data
#*********** Auther: Ahmed G. Alastal
#*********** GitHup Rep.: https://github.com/aalastal/Explore_US_Bikeshare_Data_Project

# Import required packages
import time
import pandas as pd
import numpy as np

# Creating a dictionary containing a data  for the three cities
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#Creating a List to store the months including the 'all' option  
MONTH_DATA = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

#Creating a list to store the days including the 'all' option
DAY_DATA= ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']


#*******************************************************
#Use this function to filtering user's requirements
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    #Initializing an empty city variable
    city = ''
    
    # Running this loop to ensure the correct user input of city
    while city not in CITY_DATA.keys():

        city = input("\nWhich city would you like to filter by? new york city, chicago or washington?\n").strip()
        
        #Converting user input into lower case
        city = city.lower()

        if city not in CITY_DATA.keys():
            print("This is not a valid city name please re-enter (chicago, new york city and washington)")

    #Initializing an empty month variable
    month = ''
    
    # Running this loop to ensure the correct user input of month
    while month not in MONTH_DATA:
        
        month = input("Which month would you like to filter by? January, February, March, April, May, June or type 'all' if you do not have any preference?\n").strip()
        
        #Converting user input into lower case
        month = month.lower()

        if month not in MONTH_DATA:
            print("This is not a valid month please re-enter from (january, february, ... , june) or all")

    #Initializing an empty day variable
    day = ''
    
    # Running this loop to ensure the correct user input of day
    while day not in DAY_DATA:
        day = input("Which day would you like to filter by? Saturday,Sunday, Monday, Tuesday, Wednesday, Thursday, Friday  or type 'all' if you do not have any preference.\n").strip()
        
        #Converting user input into lower case
        day = day.lower()

        if day not in DAY_DATA:
            print("\nThis is not a valid day please re-enter from (saturday, sunday, monday, ... , Friday) or all")
   
    print("\n You have chosen to view data for city: {}, month/s: {} and day/s: {}.".format(city.upper(),month.upper(), day.upper()))
    print('-'*40)
    
    #Returning the city, month and day selections
    return city, month, day


#*******************************************************
#This Function used to load data files
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        param1 (str): name of the city to analyze
        param2 (str): name of the month to filter by, or "all" to apply no month filter
        param3 (str): name of the day of week to filter by, or "all" to apply no day filter

    Returns:
        df: Pandas DataFrame containing city data filtered by month and day
    """
    start_time = time.time()

    #Load data for city file
    print("\nLoading data from the Excel file of {} city...".format(city.upper()))
    df = pd.read_csv(CITY_DATA[city])

    #Convert the Start and End Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    #Extract month and day of week from Start Time to create new columns
    #df['month'] = df['Start Time'].dt.month
    #df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['month'] = df['Start Time'].apply(lambda x: x.month)
    df['day_of_week'] = df['Start Time'].apply(lambda x: x.strftime('%A').lower())

    #Filter by month if applicable
    if month != 'all':
        #Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        #Filter by month to create the new dataframe
        df = df.loc[df['month'] == month,:]

    #Filter by day of week if applicable
    if day != 'all':
        #Filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day,:]

    #Prints the time taken to load Data
    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*40)

    #Returns the selected file as a dataframe (df) with relevant columns
    return df


#*******************************************************
#This function Displays statistics on the most frequent times of travel for the chosen data
def time_stats(df):
    """Displays statistics on the most frequent times of travel.

    Args:
        param1 (df): The data frame you intend to operate on.

    Returns:
        None.
    """
    print('\nDisplaying the statistics on the most frequent times of travel...\n')
    start_time = time.time()

    # Uses the mode method to display the most common month
    common_month = df['month'].mode()[0]
    print("Using the chosen filters, the most common month is: {}".format(common_month))

    # Uses the mode method to display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("Using the chosen filters, the most common day of the week is: {}".format(common_day))

    #Extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    #Uses mode method to display the most common hour
    common_hour = df['hour'].mode()[0]
    print('Using the chosen filters, the most common start hour is: {}'.format(common_hour))

    #Prints the time taken to perform the calculation
    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*40)
    

#*******************************************************
#This function displays statistics on the most popular stations and trip for the chosen data
def station_stats(df):
    """Displays statistics on the most popular stations and trip.

    Args:
        param1 (df): The data frame you intend to operate on.

    Returns:
        None.
    """
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #Uses mode method to display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Using the chosen filters, the most common start station is: {}'.format(common_start_station))

    #Uses mode method to display the most common end station
    common_end_station = df['End Station'].mode()[0]
    print('Using the chosen filters, The most commonly used end station is: {}'.format(common_end_station))

    #Uses str.cat to combine two columsn in the df
    #Assigns the result to a new column 'Start To End'
    #Uses mode on this new column to display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    freq_combination  = df['Start To End'].mode()[0]
    print("Using the chosen filters, the most common most frequent combination is",format(freq_combination))

    #Prints the time taken to perform the calculation
    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*40)
    

#*******************************************************
#This function displays statistics on the total and average trip duration for the chosen data
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    
     Args:
        param1 (df): The data frame you intend to operate on.

    Returns:
        None.
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #Uses sum method to calculate the total trip duration
    total_duration = df['Trip Duration'].sum()
    #Finds out the duration in minutes and seconds format
    minute, second = divmod(total_duration, 60)
    #Finds out the duration in hour and minutes format
    hour, minute = divmod(minute, 60)
    print("Using the chosen filters, the total travel time is: {} hours, {} minutes and {} seconds.".format(hour,minute,second))
    
    #Calculating the average trip duration using mean method
    mean_travel_time = df['Trip Duration'].mean()
    #Finds the average duration in minutes and seconds format
    mean_travel_time = (str(int(mean_travel_time//60)) + ' minutes ' +
                        str(int(mean_travel_time % 60)) + ' seconds')
    print("Using the chosen filters, the mean travel time is : {}".format(mean_travel_time))

    #Prints the time taken to perform the calculation
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#*******************************************************
#This function displays statistics on bikeshare users for the chosen data
def user_stats(df):
    """Display statistics on bikeshare users.
    
     Args:
        param1 (df): The data frame you intend to operate on.

    Returns:
        None.
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    #The total users are counted using value_counts method
    user_types = df['User Type'].value_counts().to_string()
    print("Using the chosen filters, the distribution for user types: {}.".format(user_types))


    # Display counts of gender
    #This try clause is implemented to display the numebr of users by Gender, becouse not every df have the Gender column
    try:
        gender_distribution = df['Gender'].value_counts().to_string()
        print("Using the chosen filters, the distribution for each gender: {}.".format(gender_distribution))
    except KeyError:
        print("We're sorry! There is no 'Gender' column in this file")

    # Display earliest, most recent, and most common year of birth
    #This try clause is is there to ensure  df containing 'Birth Year' column
    try:
        earliest_birth_year = str(int(df['Birth Year'].min()))
        print("Using the chosen filters, The earliest year of birth is: {}.".format(earliest_birth_year))
        
        most_recent_birth_year = str(int(df['Birth Year'].max()))
        print("Using the chosen filters, The most recent year of birth is: {}.".format(most_recent_birth_year))
        
        most_common_birth_year = str(int(df['Birth Year'].mode()[0]))
        print("Using the chosen filters, The most common year of birth is: {}.".format(most_common_birth_year))
    except:
        print("We're sorry! There are no birth year details in this file.")

    #Prints the time taken to perform the calculation
    print("\nThis took {} seconds.".format((time.time() - start_time)))
    print('-'*40)
    
#*******************************************************
#This function display 5 line of sorted raw data each time
def display_row_data(df):
    """ Display 5 line of sorted raw data each time.

    Args:
        param1 (df): The data frame you intend to operate on.

    Returns:
        None.
    """
    # Initialize counter variable
    counter = 0
    get_inp = input("\nWould you like to see raw data? Enter 'yes' to continue, or press any key to cancel.\n").lower().strip()
    
    while(True):
        #This IF  sentence is used after the first time, until the user chooses to continue displaying the data or not
        if counter != 0:
            get_inp = input("Do you wish to view more raw data? Enter 'yes' to continue, or press any key to cancel.\n").lower().strip()
            
        if get_inp == 'yes':
            print(df[counter : counter+5])
            counter += 5
        else:
            break           
   

    print('-'*40)


#*******************************************************
#Main function to call all functions
def main():
    
    # Make Forloop to Repeating the operations again
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        # Call Statistic Functions
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_row_data(df)

        restart = input("\nWould you like to restart? Enter 'yes' to continue, or press any key to cancel.\n").lower().strip()
        if restart.lower() != 'yes':
            break
    
    print('-'*65 + "\nThe End, we trust you had a pleasant experience. With regards.\n" + '-'*65)

if __name__ == "__main__":
	main()

#*******************************************************
#*********************** The End ***********************
#*******************************************************
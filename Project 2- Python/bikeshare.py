import time
import pandas as pd
import numpy as np

city_data = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('\nWhich city would you like to see data on?\nYour choices are: New York City, Washington, Chicago.\n\nYour Choice: ')
    city = city.casefold()
    
    while city not in city_data:
        city = input('\nThat is not a valid entry. Please try again.\nYour choices are: New York City, Washington, Chicago.\n\nYour Choice: ')
        city = city.casefold()
       
       
    # TO DO: get user input for month (all, january, february, ... , june)
    month_data = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = input('\nWhich month would you like to see data on?\nYour choices are: January, February, March, April, May, June. In case you do not wish to apply a filter, please enter \'All\'.\n\nYour Choice: ')
    month = month.casefold()
    
    while month not in month_data:
        month = input('\nThat is not a valid entry. Please try again.\nYour choices are: January, February, March, April, May, June. In case you do not wish to apply a filter, please enter \'All\'.\n\nYour Choice: ')
        month = month.casefold()
        
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_data = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input('\nWhich day would you like to see data on?\nYour choices are: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday. In case you do not wish to apply a filter, please enter \'All\'.\n\nYour Choice: ')
    day = day.casefold()
    
    while day not in day_data:
        day = input('\nThat is not a valid entry. Please try again.\nYour choices are: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday. In case you do not wish to apply a filter, please enter \'All\'.\n\nYour Choice: ')
        day = day.casefold()

    
    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Loading data file into a dataframe.
    df = pd.read_csv(city_data[city])

    
    # Create columns to display statistics
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['Start Hour'] = df['Start Time'].dt.hour

    
    #Filtering
    
    # Filtering by month (if applicable)
    if month != 'all':
        month_list = ['january', 'february', 'march', 'april', 'may', 'june']
        month = month_list.index(month) + 1
        df = df[df['month'] == month]

        
        
    # Filtering by day of week (if applicable)
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # Converting the Start Time column to datetime.
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    
    
    # TO DO: display the most common month
    
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print('Most Common Month:', months[common_month - 1])

    
    
    # TO DO: display the most common day of week
    
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    common_day = df['day_of_week'].mode()[0]
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print('Most Common Day:', days[common_day])

    
    
    # TO DO: display the most common start hour
    
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', common_hour)


    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    

    # TO DO: display most commonly used start station
    print('Most Common Start Station: ', df['Start Station'].mode()[0])
    
    
    
    # TO DO: display most commonly used end station
    print('Most Common End Station: ', df['End Station'].mode()[0])
    
    
    
    # TO DO: display most frequent combination of start station and end station trip
    common_start_end_station = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('\nMost Common Combination of Start and End Station Trips:\n\n', common_start_end_station)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    
    
    # TO DO: display total travel time
    print('Total Trip Duration:', df['Trip Duration'].sum())

    
    
    # TO DO: display mean travel time
    print('Mean Trip Duration:', df['Trip Duration'].mean())

    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*50)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types,'\n')
    
    
    
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:    
        gender = df['Gender'].value_counts()
        print(gender,'\n')
        
        
        
    # TO DO: Display earliest, most recent, and most common year of birth 
    if 'Birth Year' in df.columns:
        print('Earliest year of Birth:', df['Birth Year'].min())
        print('Latest year of Birth:', df['Birth Year'].max())
        print('Most common year of Birth:', df['Birth Year'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        
        #To prompt the user whether they would like want to see the raw data
        answers = ['yes','no']
        answer = input('\nWould you like to see more data?\nYour choices are: Yes, No.\n\nYour Choice: ')
        
        while answer.lower() not in answers:
            answer = input('\nThat is not a valid entry. Please try again.\nYour choices are: Yes, No.\n\nYour Choice: ')
            answer = answer.lower()
        
        x = 0
        
        while True :
            if answer.lower() == 'yes':
        
                print(df.iloc[x : x + 5])
                x += 5
                answer = input('\nWould you like to see more data?\nYour choices are: Yes, No.\n\nYour Choice: ')
                while answer.lower() not in answers:
                    answer = input('\nThat is not a valid entry. Please try again.\nYour choices are: Yes, No.\n\nYour Choice: ')
                    answer = answer.lower()
            else:
                break           

                
                
        restart = input('\nWould you like to restart?\nYour choices are: Yes, No.\n\nYour Choice: ')
        #check wheather the user is entering the valid entry or not
        while restart.lower() not in answers:
            restart = input('\nThat is not a valid entry. Please try again.\nYour choices are: Yes, No.\n\nYour Choice: ')
            restart = restart.lower()
        if restart.lower() != 'yes':
            print('\nThank you!')
            break


if __name__ == "__main__":
	main()

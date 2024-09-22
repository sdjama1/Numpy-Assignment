import numpy as np
import pandas

data = pandas.read_csv('/Users/yvngsaid/Desktop/players_stats_by_season_full_details.csv')

array = np.array(data)

#print(array)




#extracting the columns from the array
fgm = array[:, 8].astype(float)  #convert to float
fga = array[:, 9].astype(float)
threepm = array[:, 10].astype(float)
threepa = array[:, 11].astype(float)
ftm = array[:, 12].astype(float)
fta = array[:, 13].astype(float)
points_scored = array[:, 22].astype(float)
time_played = array[:, 7].astype(float)
blocks = array[:, 21].astype(float)
steals = array[:, 20].astype(float)
games_played = array[:, 6].astype(float)

combined_fgm = fgm + threepm + ftm
combined_fga = fga + threepa + fta



#calculating field goal accuracy
fg_accuracy = np.where(fga > 0, (fgm / fga) * 100, 0)
three_point_accuracy = np.where(threepa > 0, (threepm / threepa) * 100, 0)
free_throw_accuracy = np.where(fta > 0, (ftm / fta) * 100, 0)
average_points_per_minute = np.where(time_played > 0, points_scored / time_played, 0)
overall_shooting_accuracy = np.where(combined_fga > 0, (combined_fgm / combined_fga) * 100, 0)
average_blocks_per_game = np.where(games_played > 0, blocks / games_played, 0)
average_steals_per_game = np.where(games_played > 0, steals / games_played, 0)


#print(three_point_accuracy)
#print(average_points_per_minute)
#print(fg_accuracy)
#print(free_throw_accuracy)
#print(average_blocks_per_game)
#print(overall_shooting_accuracy)
#print(average_steals_per_game)

players = array[:, 4]
seasons = array[:, 2]
combined_data = np.column_stack((players, seasons, fg_accuracy, three_point_accuracy, free_throw_accuracy, average_points_per_minute, overall_shooting_accuracy, average_blocks_per_game, average_steals_per_game))



def topplayers(data, index, top = 100):
    sorted_data = data[data[:, index].astype(float).argsort()[::-1]]
    return sorted_data[:top]

top_fg_accuracy = topplayers(combined_data, 2)
top_three_pt_accuracy = topplayers(combined_data, 3) 
top_ft_accuracy = topplayers(combined_data, 4)
top_avg_points = topplayers(combined_data, 5)
top_overall_shooting = topplayers(combined_data, 6)
top_avg_blocks = topplayers(combined_data, 7)
top_avg_steals = topplayers(combined_data, 8)

print("Top 100 Field Goal Accuracy")
print(top_fg_accuracy)
print("Top 100 Three Point Accuracy")
print(top_three_pt_accuracy)
print("top 100 Free Throw Accuracy")
print(top_ft_accuracy)
print("Top 100 Average Points Per Minute")
print(top_avg_points)
print("Top 100 Overall Shooting Accuracy")
print(top_overall_shooting)
print("Top 100 Average Blocks Per Game")
print(top_avg_blocks)
print("Top 100 Average Steals Per Game")
print(top_avg_steals)

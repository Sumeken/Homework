temps= [
    ('Austin', 97), ('Boston',82),('Chicago',85),('Denver',90),('Las Vegas',105),('Los Angeles',82),('Miami',97),('New York',85),('Phoenix',107),('San Francisco',66)
]


print(sorted(temps, key=lambda student: student[1], reverse=True))
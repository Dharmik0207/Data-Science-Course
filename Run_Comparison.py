import matplotlib.pyplot as plt

years = [2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]

kohli = [850,980,1100,1050,1150,1250,1180,1300,1220,980]
rohit = [720,800,920,950,1020,1100,1080,1120,1090,870]
sehwag = [910,870,780,720,650,600,550,520,500,450]

plt.plot(years, kohli, color='Red', linestyle='--', label="Virat Kohli")
plt.plot(years, rohit, color='blue', linestyle='-.', label="Rohit Sharma")
plt.plot(years, sehwag, color='green', linestyle='-', label="Virendra Sehwag")
plt.title("Performance Comparison")
plt.legend()
plt.grid(True)
plt.show()
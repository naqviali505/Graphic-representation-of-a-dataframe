#!/usr/bin/env python
# coding: utf-8

# In[62]:

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df =  pd.read_csv('gas_prices.csv')


occurances=np.array(df["Year"])


r1=df["USA"]
r2=df["Canada"]
r3=df["South Korea"]
r4=df["Australia"]

plt.plot(occurances,r1, color='blue', marker='o')
plt.plot(occurances,r2, color='red', marker='o')
plt.plot(occurances,r3, color='green', marker='o')
plt.plot(occurances,r4, color='yellow', marker='o')

plt.title('Gas Prices over Time in (USD)', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.ylabel('US Dollors', fontsize=14)
plt.grid(True)
plt.show()


# In[25]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df =  pd.read_csv('fifa_data.csv')


skill= df["Overall"].dropna()



plt.title("Distribution of Player skill in FIFA 18")
plt.hist(skill)
plt.show()


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df =  pd.read_csv('fifa_data.csv')

occurances=df["Nationality"]


r1=df[df["Age"]<27]
r2=df[df["Age"]>26]

width = 0.25
plt.bar(r1["Nationality"],r1["Age"], color = 'b',
        width = width,  label='juniors')
plt.bar(r2["Nationality"], r2["Age"],color = 'r',
        width = width, edgecolor = 'black',  label='seniors')
  
plt.xlabel("Year")
plt.ylabel("Number of people ")
plt.title("Number of juniors and Seniors ")
  

plt.xticks(r ,r1["Nationality"])
plt.legend()
plt.show()


# In[ ]:


/


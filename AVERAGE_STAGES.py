import numpy as np
import matplotlib.pyplot as plt

the_stages=np.array(["FIRST-STAGE","SECOND-STAGE","THIRD-STAGE","FOURTH-STAGE","FIFTH-STAG","SIXTH-STAGE","SIVENTH-STAGE"])
the_success_rate=np.array([8,7.5,6,7.3,5,9,9.7])

# PIE
plt.style.use("bmh")
plt.pie(
    the_success_rate,labels=the_stages,explode=[0.1,0,0.1,0,0.1,0,0],
    labeldistance=1.1,radius=1,
    colors=["red","green","blue","yellow","gray","brown","pink"],
    startangle=1,rotatelabels=False,autopct="%1.0f%%",shadow=1,counterclock=0
)
plt.title("SUCCESS_RATE",color="red")
plt.show()
import pandas as pd
import os
from jpype import *
import numpy as np

GerMexTweets = pd.read_csv("germex_translated.csv", parse_dates = ["created_at"])

import json
trees=[]
with open('ReplyTrees.txt', "r") as f:
    for line in f:
        trees.append(eval(line))


cascade_stats = pd.read_csv("cascade_stats.csv").iloc[:,1:]
cascade_stats["root"] = cascade_stats.root.apply(lambda t: eval(t)[0])
from datetime import datetime

r = GerMexTweets.reset_index()[GerMexTweets.reset_index()["id_str"].isin(cascade_stats.root.tolist())]["created_at"]
r = r.apply(lambda t: datetime.strptime(t, "%a %b %d %H:%M:%S +0000 %Y"))

cascade_stats["root_created_at"] = r.reset_index().iloc[:,1]
cascade_stats.head()

import  matplotlib.pyplot as plt
cascade_stats.set_index("root_created_at").virality.plot()
plt.show()

jarLocation = os.path.join(os.getcwd(), "infodynamics-jar-1.4", "infodynamics.jar")
if (not(os.path.isfile(jarLocation))):
    exit("infodynamics.jar not found (expected at " + os.path.abspath(jarLocation) + ") - are you running from demos/python?")
startJVM(getDefaultJVMPath(),"-Xmx6G" ,"-ea", "-Djava.class.path=" + jarLocation)
teCalcClass = JPackage("infodynamics.measures.continuous.kernel").TransferEntropyCalculatorKernel
teCalc = teCalcClass()




transcript_effects = pd.read_csv("transcript_effects.csv", parse_dates=["time"]).set_index("time").resample("S").max().fillna(0)
vir = cascade_stats.set_index("root_created_at")["virality"].resample("S").max().fillna(0)
vol = cascade_stats.set_index("root_created_at")["volume"].resample("S").max().fillna(0)


transcript_effects = transcript_effects.join(vir, how="inner").join(vol, how="inner").fillna(0)
transcript_effects["tot"] = transcript_effects.Germany.abs() + transcript_effects.Mexico.abs()
print(transcript_effects.head())

for k in range (1, 12):
    k = k * 5
    print (f"K is {k} seconds")
    teCalc = teCalcClass()
    teCalc.setProperty("NORMALISE", "true") # Normalise the individual variables
    teCalc.initialise(k, 0.5)
    teCalc.setObservations(JArray(JDouble, 1)(transcript_effects.Germany.tolist()), JArray(JDouble, 1)(transcript_effects.virality.tolist()))
    t_vir_ger = teCalc.computeAverageLocalOfObservations()
    print(f"TE Transcript Effects to Germany to Virality {t_vir_ger}")
    teCalc = teCalcClass()
    teCalc.setProperty("NORMALISE", "true") # Normalise the individual variables
    teCalc.initialise(k, 0.5)
    teCalc.setObservations(JArray(JDouble, 1)(transcript_effects.Germany.tolist()), JArray(JDouble, 1)(transcript_effects.volume.tolist()))
    t_vol_ger = teCalc.computeAverageLocalOfObservations()
    print(f"TE Transcript Effects to Germany to Volume {t_vol_ger}")

    teCalc = teCalcClass()
    teCalc.setProperty("NORMALISE", "true") # Normalise the individual variables
    teCalc.initialise(k, 0.5)
    teCalc.setObservations(JArray(JDouble, 1)(transcript_effects.Mexico.tolist()), JArray(JDouble, 1)(transcript_effects.virality.tolist()))
    t_vir_mex = teCalc.computeAverageLocalOfObservations()
    print(f"TE Transcript Effects to Mexico to Virality {t_vir_mex}")
    teCalc = teCalcClass()
    teCalc.setProperty("NORMALISE", "true") # Normalise the individual variables
    teCalc.initialise(k, 0.5)
    teCalc.setObservations(JArray(JDouble, 1)(transcript_effects.Mexico.tolist()), JArray(JDouble, 1)(transcript_effects.volume.tolist()))
    t_vol_mex = teCalc.computeAverageLocalOfObservations()
    print(f"TE Transcript Effects to Mexico to Volume {t_vol_mex}")


    teCalc = teCalcClass()
    teCalc.setProperty("NORMALISE", "true") # Normalise the individual variables
    teCalc.initialise(k, 0.5)
    teCalc.setObservations(JArray(JDouble, 1)(transcript_effects.tot.tolist()), JArray(JDouble, 1)(transcript_effects.virality.tolist()))
    t_vir_tot = teCalc.computeAverageLocalOfObservations()
    print(f"TE Transcript Effects to Both German and Mexico to Virality {t_vir_tot}")
    teCalc = teCalcClass()
    teCalc.setProperty("NORMALISE", "true") # Normalise the individual variables
    teCalc.initialise(k, 0.5)
    teCalc.setObservations(JArray(JDouble, 1)(transcript_effects.tot.tolist()), JArray(JDouble, 1)(transcript_effects.volume.tolist()))
    t_vol_tot = teCalc.computeAverageLocalOfObservations()
    print(f"TE Transcript Effects to Both German and Mexico to Volume {t_vol_tot}")
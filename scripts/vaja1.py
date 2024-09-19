#! /usr/bin/python3
import json, yaml
import pickle as pkl
import numpy as np
import matplotlib.pylab as plt
import time as space

global zgodovina
zgodovina = []

def main():
    global zgodovina
    while True:
        vhod = input("Izberite opcijo:\na) sestevanje\nb) odstevanje\nq) izhod\nVnos: ")
        if vhod =="a":
            a = float(input("Vnesite številko a (a+b): "))
            b = float(input("Vnesite številko b (a+b): "))
            rezultat = {"a":a, "b":b, "r":a+b}
            zgodovina.append(rezultat)
            print(f"rezultat: {a+b}")
        elif vhod == "b":
            a = float(input("Vnesite številko a (a-b): "))
            b = float(input("Vnesite številko b (a-b): "))
            rezultat = {"a":a, "b":b, "r":a-b}
            zgodovina.append(rezultat)
            print(f"rezultat: {a-b}")
        elif vhod == "q":
            with open("../log.txt", "w") as f:
                f.writelines(yaml.dump(zgodovina))
            break
        else:
            print("Vnesite veljavno črtko!")




if __name__ == "__main__":
    main()
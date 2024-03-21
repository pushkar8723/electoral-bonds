Electoral Bonds
===============

Ported electoral bonds data released by SBI & ECI (in PDF format) to CSV and MySQL DB (to make it easier to read and analyze).

ECI disclosed this data [here](https://www.eci.gov.in/disclosure-of-electoral-bonds)

This intends to make the data more accessible for analysis using MS Excel or similar tools.

Supreme court registry data is unfortunately not in a format that can be easily ported to CSV. It doesn't follow any fixed format and mostly consists of a scan of political parties' declarations.

---

### Dashboard

Besides migrating the data to CSV and MySQL DB, I also created a dashboard using [Metabase](https://github.com/metabase). This dashboard can be easily run and accessed locally and it also supports a few filters.

To run the dashboard locally you would need `docker` and `docker-compose` installed on your system.
On Windows and Mac, these can be installed using [Docker Desktop](https://www.docker.com/products/docker-desktop/). 
On Linux, you can choose to use Docker desktop or install both `docker` and `docker-compose` using the distro's official package manager.

Once docker is installed on your system run the following command in the `dashboard` directory to run the dashboard

```
docker-compose up
```

[Dashboard Link](http://localhost:3000/public/dashboard/f1201124-1063-427c-8d98-511578b73159)


[Furthur Instructions to run/update the dasbhoard](https://github.com/pushkar8723/electoral-bonds/tree/main/dashboard)

Note: The dashboard is independent of the Python script. Thus you can directly run the dashboard by following the instructions above.

![image](https://github.com/pushkar8723/electoral-bonds/assets/2996493/c30a4c5d-8273-4fba-bdfb-cd0880d216fe)

![image](https://github.com/pushkar8723/electoral-bonds/assets/2996493/a7ac8933-1794-4ca0-a121-890afb28b954)

![image](https://github.com/pushkar8723/electoral-bonds/assets/2996493/9826a0f6-1b13-4fcf-a033-804e4d76c9bc)

![image](https://github.com/pushkar8723/electoral-bonds/assets/2996493/eb1af64f-89cb-4ec9-9864-69c6c2ed050b)

![image](https://github.com/pushkar8723/electoral-bonds/assets/2996493/d1959db0-182b-41d4-824b-14153cea34e8)

---

### Data & Output

I included the PDFs released by ECI inside the `data` directory and the corresponding CSVs in the `output` directory.

#### Script

I wrote `main.py` which converted the PDFs to CSVs.
The following are the prerequisites to run this Python file.
- Python 3.8+
- Java 8+
- [Tabula Python module](https://github.com/tabulapdf/tabula)

To run the script run 
```sh
python main.py
```

This will
- convert `data/purchase-full-disclosure.pdf` to `output/purchase-full-disclosure.csv`
- convert `data/encashed-full-disclosure.pdf` to `output/encashed-full-disclosure.csv`  

---

##### Disclaimer

- I only changed the format of the data released by ECI and have not manipulated it in any way.
- I have also included the script I wrote for conversion.
- I don't have any affiliation to any political party/individual. 

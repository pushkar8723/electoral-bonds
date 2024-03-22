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

![image](https://github.com/pushkar8723/electoral-bonds/assets/2996493/2fa8deb9-0fce-4ee3-b688-67bd8e8c2dc0)

![image](https://github.com/pushkar8723/electoral-bonds/assets/2996493/3e6eb4dc-3d18-4230-93d8-644bf82eace3)

![image](https://github.com/pushkar8723/electoral-bonds/assets/2996493/7c50c345-5f68-4705-8c12-7a33dd3d647f)

![image](https://github.com/pushkar8723/electoral-bonds/assets/2996493/9cc8a758-ea03-4947-9b95-1b1dbe4ba75f)

![image](https://github.com/pushkar8723/electoral-bonds/assets/2996493/44959826-40ea-4f57-b352-c3fb158c0530)

![image](https://github.com/pushkar8723/electoral-bonds/assets/2996493/f0824ee7-d843-4904-b2f0-008997fe1d97)


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

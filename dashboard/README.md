Dashboard
=========

I also collated the data and made 2 dashboards. One for the purchaser and one for the receiver (en-casher).
For this, I imported the CSV files into MySQL db and used [Metabase](https://github.com/metabase) to create these dashboards.
These dashboards can be easily accessed by running the docker containers.

---

### Running dashboard

Make sure you have `docker` and `docker-compose` installed on your system.
After that run the following command:

```
docker-compose up
```

Click on the link below to access the dashboards
- [Purchase](http://localhost:3000/public/dashboard/8fdcaa0f-66de-4e60-8ffb-0e0d4bbca8e2)
- [Encashed](http://localhost:3000/public/dashboard/104cde10-40b4-4d16-a2ba-c7c3b109c614)

---

### Creating / Updating the dashboard

Then you can access Metabase @ [localhost:3000](http://localhost:3000/)

To log in, enter the following credentials:
- Email: admin@pushkaranand.com
- Password: p@ssw0rd1

---

### Connect to MySQL database

Running `docker-compose up` command will also expose the MySQL DB.

You can use the following credentials to connect to it.
- user: root
- password: p@ssw0rd
- db: electoral-bonds

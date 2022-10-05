<p align="center">
  <a href="" rel="noopener">
 <img width=720px height=400px src="https://drive.google.com/uc?export=view&id=1WvXt1Z7dzrPKLQUh4vAhT_Mq7sha-hEc" alt="Project logo - stable diffusion"></a>
</p>

<h1 align="center">Futbol</h1>

<div align="center">

</div>

<p align="center"> This project has been designed to be the backend of the futbol project.
    <br> 
</p>

---

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [TODO](../#todo)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

This project intends to have a follow-up of young players to make better decisions when signing for the youth soccer club. This project has been deployed to AWS and is currently used by over 50 scouts distributed in Europe creating networking between them.

[futbol](https://github.com/fran-roca/futbol) and [futbol_web](https://github.com/fran-roca/futbol_web) was developed in 3 weeks to help a frind with his use case. It was released to production with the minimum number of features and will be improved in the future as will need. There are some features that are pending to do in the short time [TODO](../#todo). Also this project was a prove of concept to develop a project made with python and deployed in AWS for this reason might be some improvements in the code, as I said it will be improved as my knoledge improve.

## 🏁 Getting Started <a name = "getting_started"></a>

### Prerequisites

- Have a look to [requirements](requirements.txt)
- You must have a MySQL database created, you can find the script [here](model\scripts).
<br/>
<a href="https://github.com/fran-roca/futbol/blob/d6d6e26ed651f6ef296e2a15296046757c19da28/model/model.png" rel="noopener">
 <img width=700px height=600px src="model\model.png" alt="Model"></a>
 <br/>

### Installing

1. Clone the repo
   ```sh
   git clone https://github.com/fran-roca/futbol
   ```
2. Install NPM packages
   ```sh
   pip install -r requirements.txt
   ```
3. Add enviroment properties, for local create a file local.properties

   ```sh
   {
      "enviroment": "local",
      "port": "8000",
      "SQLALCHEMY_DATABASE_URI": "mysql+pymysql://user:pass@db_url",
      "SECRET_KEY": "keygen_to_encript_password"
    }
   ```
## 🎈 Usage <a name="usage"></a>

Once it is deployed, you can use postman to call to the endpoints. Documentation of the endpoints is in progress.

## TODO <a name="todo"></a>
- Documentation
- Test

## 🚀 Deployment <a name = "deployment"></a>

Futbol is divided into 3 modules and deployed in AWS:
- Database [MySQL](model\scripts) - EC2
- Backend [futbol](https://github.com/fran-roca/futbol) - Elastic Beanstalk
- Frontend [futbol_web](https://github.com/fran-roca/futbol_web) - AWS Amplify

## ⛏️ Built Using <a name = "built_using"></a>

- [AWS](https://aws.amazon.com/) - Hosting Services
- [SQLAlchemy](https://www.sqlalchemy.org/) - Database query engine
- [Flask](https://flask.palletsprojects.com/) - Web Framework
- [Python](https://www.python.org/) - Programming language

## ✍️ Authors <a name = "authors"></a>

- [@fran-roca](https://github.com/fran-roca) - Idea & Initial work

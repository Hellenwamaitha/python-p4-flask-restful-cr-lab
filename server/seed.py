#!/usr/bin/env python3

from app import app, db
from models import db,Plant  # Import the Plant model

with app.app_context():
    db.create_all()  # Create the database tables if they don't exist

    Plant.query.delete()

    # Create Plant instances and add them to the session
    aloe = Plant(
        id=1,
        name="Aloe",
        image="./images/aloe.jpg",
        price=11.50,
    )

    emerald_snake = Plant(
        id=2,
        name="Emerald snake",
        image="https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcQHttSM__yX420_BQdhFvQrEsdjipRUtLpIlrGNkUtKnFbb5M-10tCoAAflIjFMgY2GP09nZOY9cDFd0gdGDrc1ZJd5YzW94FHXh1juy_v87HKvlnbQ8JsCud1KLNuoQ7dsElDvGLqn8tY&usqp=CAc",
        price=25.98,
    )

    succulents = Plant(
        id=3,
        name="Succulents",
        image="https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcQKCY8E6Ht0Vxq0yM1YfluyTjcL3W9GlfZXMDL4o4Zr5zAjKxdGh_nI5qOrhWl5Cg-_D1G_29MqR51hhKaHAu0gwisymF1cfwYMa_0BoVxnqEY0_4vlRk1nxQ&usqp=CAc",
        price=14.50,
    )

    odessa = Plant(
        id=4,
        name="Odessa",
        image="https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcSn-kEiCM3KB6jcd6QYNKKrojJG7qCNablPPbOjiLPBocxVE8lNTa_3_V7DwY9eV2M9ewfv3THA66uaebdwcmE6SFoUuMNKTPCX0dqIjTlGeiaMXRj1I0-cWLKe8Q5B&usqp=CAc",
        price=17.55,
    )

    factory_herb = Plant(
        id=5,
        name="Factory Herb",
        image="https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcQCpHH4TDJkE0fW_OIi2HajHyovNh8TX5eGNuu4klQPc8iNhpnPdTI3Fl8ld687sLZGJuU4VZKP1HsusbpDDNKi6pe5A_XsBdjlp4sYcG2ING5ZkhYKSmyh3KBAFsMMG5XeS_wDVU8waHI&usqp=CAc",
        price=90.30,
    )

    db.session.add_all([aloe, emerald_snake, succulents, odessa, factory_herb])
    db.session.commit()

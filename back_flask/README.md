## To launch 

$ pipenv shell
$ python run.py

## PROD
pipenv install
pipenv shell
pm2 start run.py


## REST API

['POST'] Create User
http://localhost:3030/api/v1/<user_id> 
+ config -> JSON

['GET'] GET User config
http://localhost:3030/api/v1/config/<user_id> 
GET config -> JSON

['PUT'] Add answers to User
http://localhost:3030/api/v1/<user_id> 
+ data

['DELETE'] delete User
http://localhost:3030/api/v1/<user_id> 



## SQL

* Create Table

-- Table: public.perception_ux

-- DROP TABLE public.perception_ux;

-- Table: public.perception_ux

-- DROP TABLE public.perception_ux;

CREATE TABLE public.perception_ux
(
    id_poste integer NOT NULL,
    config json NOT NULL,
    age integer,
    genre integer,
    education integer,
    education_other character varying(128) COLLATE pg_catalog."default",
    location integer,
    location_zipcode integer,
    location_density integer,
    grew integer,
    grew_zipcode integer,
    grew_density integer,
    grew_country character varying(128) COLLATE pg_catalog."default",
    frequency_3d integer,
	technology_3d integer[],
    technology_3d_other character varying(128) COLLATE pg_catalog."default",
    participation integer,
    participation_3d integer,
	participation_role integer[],
    participation_role_other character varying(128) COLLATE pg_catalog."default",
    participation_sujet integer,
    participation_sujet_other character varying(128) COLLATE pg_catalog."default",
    participation_number integer,
    colorblind_rg integer,
    colorblind_dc integer,
	colorblind_pt integer,
    exercice_3d integer,
    "E0Q0" integer,
    "E0Q1" integer,
    "E0Q2" integer,
    "E1Q0" integer,
    "E1Q1" integer,
    "E1Q2" integer,
    "E1Q3" integer,
    "E1Q4" integer,
    "E0Time" integer,
    "E1Time" integer,
    smile integer,
    difficulty integer,
    opinion3dpart integer,
    comment character varying(1024) COLLATE pg_catalog."default",
    followup integer,
    email character varying(256) COLLATE pg_catalog."default",
    CONSTRAINT perception_ux_pkey PRIMARY KEY (id_poste)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.perception_ux
    OWNER to postgres;
'''

* Create user

INSERT INTO public.perception_ux(
	id_poste, config, age, genre, education, education_other, location, location_zipcode, location_density, grew, grew_zipcode, grew_density, grew_country, frequency_3d, technology_3d, technology_3d_other, participation, participation_3d, participation_role, participation_role_other, participation_sujet, participation_sujet_other, participation_number, colorblind_rg, colorblind_dc, exercice_3d, "E1Q1", "E1Q2", "E1Q3")
	VALUES (12, '{"lod":[1,2],"style":[1,2,3],"answer":[1,2,3,5,6]}', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null);
'''


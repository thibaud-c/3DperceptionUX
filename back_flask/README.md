## To launch 

$ pipenv shell
$ python run.py

## PROD
pipenv install
pipenv shell
pipenv install python-dotenv
pm2 start run.py


## REST API

['POST'] Create User
http://localhost:1337/api/v1/<user_id> 
+ config -> JSON

['GET'] GET User config
http://localhost:1337/api/v1/config/<user_id> 
GET config -> JSON

['PUT'] Add answers to User
http://localhost:1337/api/v1/<user_id> 
+ data

['DELETE'] delete User
http://localhost:1337/api/v1/<user_id> 



## SQL

-- Table: public.perception_ux

-- DROP TABLE public.perception_ux;

CREATE TABLE public.perception_ux
(
    user_guid character varying(36) COLLATE pg_catalog."default",
    start_at timestamp with time zone,
    end_at timestamp with time zone,
    language integer,
    version integer,
    scenes_order integer[],
    answers_order integer[],
    angles_order real[],
    user_tech_config json,
    age integer,
    gender integer,
    education integer,
    grew_density integer,
    grew_country character varying(128) COLLATE pg_catalog."default",
    location_density integer,
    location_country character varying(128) COLLATE pg_catalog."default",
    frequency_3d integer,
    exercice_spatial integer,
    tuto_time integer,
    "E0Q0" json,
    "E0Q1" json,
    "E0Q2" json,
    "E1Q0" json,
    "E1Q1" json,
    "E1Q2" json,
    "E2Q0" json,
    "E2Q1" json,
    "E2Q2" json,
    "E2Q3" json,
    "E3Q0" json,
    "E3Q1" json,
    "E3Q2" json,
    "E3Q3" json,
    pref_hard integer,
    pref_easy integer,
    pref_memory integer,
    pref_static integer,
    estim_building integer,
    smile integer,
    difficulty integer,
    comment character varying(1024) COLLATE pg_catalog."default",
    followup integer,
    email character varying(256) COLLATE pg_catalog."default"

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


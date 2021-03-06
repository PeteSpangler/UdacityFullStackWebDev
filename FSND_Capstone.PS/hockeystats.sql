--
-- PostgreSQL database dump
--

-- Dumped from database version 12.4
-- Dumped by pg_dump version 12.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Goalies; Type: TABLE; Schema: public; Owner: peter
--

CREATE TABLE public."Goalies" (
    id integer NOT NULL,
    name character varying(256),
    gaa double precision,
    so integer,
    w integer
);


ALTER TABLE public."Goalies" OWNER TO peter;

--
-- Name: Goalies_id_seq; Type: SEQUENCE; Schema: public; Owner: peter
--

CREATE SEQUENCE public."Goalies_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Goalies_id_seq" OWNER TO peter;

--
-- Name: Goalies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: peter
--

ALTER SEQUENCE public."Goalies_id_seq" OWNED BY public."Goalies".id;


--
-- Name: Skaters; Type: TABLE; Schema: public; Owner: peter
--

CREATE TABLE public."Skaters" (
    id integer NOT NULL,
    name character varying(256),
    pos character varying(20),
    pts integer,
    gls integer
);


ALTER TABLE public."Skaters" OWNER TO peter;

--
-- Name: Skaters_id_seq; Type: SEQUENCE; Schema: public; Owner: peter
--

CREATE SEQUENCE public."Skaters_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Skaters_id_seq" OWNER TO peter;

--
-- Name: Skaters_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: peter
--

ALTER SEQUENCE public."Skaters_id_seq" OWNED BY public."Skaters".id;


--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: peter
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO peter;

--
-- Name: Goalies id; Type: DEFAULT; Schema: public; Owner: peter
--

ALTER TABLE ONLY public."Goalies" ALTER COLUMN id SET DEFAULT nextval('public."Goalies_id_seq"'::regclass);


--
-- Name: Skaters id; Type: DEFAULT; Schema: public; Owner: peter
--

ALTER TABLE ONLY public."Skaters" ALTER COLUMN id SET DEFAULT nextval('public."Skaters_id_seq"'::regclass);


--
-- Data for Name: Goalies; Type: TABLE DATA; Schema: public; Owner: peter
--

COPY public."Goalies" (id, name, gaa, so, w) FROM stdin;
1	Corey Crawford	0.923	7	20
2	Corey Hart	0.912	2	17
3	Carey Price	0.932	12	37
4	Ben Bishop	0.873	3	11
5	Tukka Rask	0.853	1	15
\.


--
-- Data for Name: Skaters; Type: TABLE DATA; Schema: public; Owner: peter
--

COPY public."Skaters" (id, name, pos, pts, gls) FROM stdin;
1	Austen Matthews	C	12	37
2	Connor McDavid	C	32	87
3	Taylor Hall	RW	42	77
4	Elias Petterssen	LW	22	50
5	Duncan Keith	D	42	8
6	Cale Makar	D	52	12
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: peter
--

COPY public.alembic_version (version_num) FROM stdin;
\.


--
-- Name: Goalies_id_seq; Type: SEQUENCE SET; Schema: public; Owner: peter
--

SELECT pg_catalog.setval('public."Goalies_id_seq"', 5, true);


--
-- Name: Skaters_id_seq; Type: SEQUENCE SET; Schema: public; Owner: peter
--

SELECT pg_catalog.setval('public."Skaters_id_seq"', 6, true);


--
-- Name: Goalies Goalies_pkey; Type: CONSTRAINT; Schema: public; Owner: peter
--

ALTER TABLE ONLY public."Goalies"
    ADD CONSTRAINT "Goalies_pkey" PRIMARY KEY (id);


--
-- Name: Skaters Skaters_pkey; Type: CONSTRAINT; Schema: public; Owner: peter
--

ALTER TABLE ONLY public."Skaters"
    ADD CONSTRAINT "Skaters_pkey" PRIMARY KEY (id);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: peter
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- PostgreSQL database dump complete
--


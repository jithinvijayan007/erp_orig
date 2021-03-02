CREATE TABLE customer_rating (
    pk_bint_id BIGSERIAL PRIMARY KEY,
    vchr_feedback TEXT NULL,
    dbl_rating DOUBLE PRECISION ,
    fk_customer_id BIGINT REFERENCES customer_details (pk_bint_id) NOT NULL,
    fk_user_id BIGINT REFERENCES userdetails ( user_ptr_id) NOT NULL
);
CREATE TABLE emp_category(
  pk_bint_id BIGSERIAL PRIMARY KEY,
  vchr_code VARCHAR(10),
  vchr_name VARCHAR(150),
  int_status INTEGER ,
  fk_created_id BIGINT REFERENCES auth_user(id),
  fk_updated_id BIGINT REFERENCES auth_user(id),
  dat_created TIMESTAMP ,
  dat_updated TIMESTAMP
);

ALTER TABLE userdetails
DROP COLUMN fk_category_id;

ALTER TABLE userdetails
ADD COLUMN fk_category_id BIGINT REFERENCES emp_category(pk_bint_id);


CREATE TABLE staff_rating (
    pk_bint_id BIGSERIAL PRIMARY KEY,
    vchr_remarks TEXT NULL,
    dbl_rating DOUBLE PRECISION ,
    fk_enquiry_master_id BIGINT REFERENCES enquiry_master(pk_bint_id) NOT NULL,
    fk_user_id BIGINT REFERENCES userdetails ( user_ptr_id) NOT NULL,
    fk_customer_id BIGINT REFERENCES customer_details (pk_bint_id) NOT NULL
);
ALTER TABLE staff_rating
ADD COLUMN vchr_staff_attitude varchar(50) NOT NULL,
ADD COLUMN vchr_staff_knowledge varchar(50) NOT NULL,
ADD COLUMN vchr_store_ambience varchar(50) NOT NULL,
ADD COLUMN vchr_recommended varchar(50) NOT NULL;

alter table staff_rating add column vchr_know_about VARCHAR(50);

ALTER TABLE staff_rating RENAME COLUMN vchr_remarks TO vchr_comments;

CREATE TABLE gdp_details(
                        pk_bint_id BIGSERIAL PRIMARY KEY,
                        dbl_from DOUBLE PRECISION,                         
                        dbl_to DOUBLE PRECISION,
                        dbl_amt DOUBLE PRECISION,
                        int_type INTEGER,
                        fk_product_id BIGINT REFERENCES products
                       );

ALTER TABLE products ADD COLUMN jsn_warranty JSONB; 


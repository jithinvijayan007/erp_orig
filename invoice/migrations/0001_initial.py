# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-05-29 15:35
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustServiceDelivery',
            fields=[
                ('pk_bint_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('vchr_cust_name', models.CharField(blank=True, max_length=100, null=True)),
                ('int_mobile', models.BigIntegerField(blank=True, null=True)),
                ('txt_address', models.TextField(blank=True, null=True)),
                ('vchr_landmark', models.CharField(blank=True, max_length=200, null=True)),
                ('vchr_gst_no', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'cust_service_delivery',
            },
        ),
        migrations.CreateModel(
            name='LoyaltyCardInvoice',
            fields=[
                ('pk_bint_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('int_points', models.BigIntegerField(blank=True, null=True)),
                ('dbl_amount', models.FloatField(blank=True, null=True)),
                ('dat_invoice', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'loyalty_card_invoice',
            },
        ),
        migrations.CreateModel(
            name='PartialInvoice',
            fields=[
                ('pk_bint_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('json_data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('int_active', models.IntegerField(blank=True, default=0, null=True)),
                ('dat_created', models.DateTimeField(blank=True, null=True)),
                ('dat_invoice', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'partial_invoice',
            },
        ),
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('pk_bint_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('int_fop', models.IntegerField()),
                ('vchr_card_number', models.CharField(blank=True, max_length=20, null=True)),
                ('vchr_name', models.CharField(blank=True, max_length=100, null=True)),
                ('vchr_finance_schema', models.CharField(blank=True, max_length=20, null=True)),
                ('vchr_reff_number', models.CharField(blank=True, max_length=100, null=True)),
                ('dbl_receved_amt', models.FloatField(blank=True, null=True)),
                ('dbl_finance_amt', models.FloatField(blank=True, null=True)),
                ('dat_created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'managed': False,
                'db_table': 'payment_details',
            },
        ),
        migrations.CreateModel(
            name='SalesDetails',
            fields=[
                ('pk_bint_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('int_qty', models.IntegerField(blank=True, null=True)),
                ('dbl_amount', models.FloatField(blank=True, null=True)),
                ('dbl_tax', models.FloatField(blank=True, null=True)),
                ('dbl_discount', models.FloatField(blank=True, null=True)),
                ('dbl_buyback', models.FloatField(blank=True, null=True)),
                ('json_tax', django.contrib.postgres.fields.jsonb.JSONField()),
                ('vchr_batch', models.CharField(blank=True, max_length=50, null=True)),
                ('json_imei', django.contrib.postgres.fields.jsonb.JSONField()),
                ('int_doc_status', models.IntegerField(blank=True, null=True)),
                ('dbl_supplier_amount', models.FloatField(blank=True, null=True)),
                ('dbl_selling_price', models.FloatField(blank=True, null=True)),
                ('int_sales_status', models.IntegerField(blank=True, null=True)),
                ('dbl_indirect_discount', models.FloatField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'sales_details',
            },
        ),
        migrations.CreateModel(
            name='SalesMaster',
            fields=[
                ('pk_bint_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('dat_invoice', models.DateField(blank=True, null=True)),
                ('vchr_invoice_num', models.CharField(blank=True, max_length=50, null=True)),
                ('vchr_remarks', models.CharField(blank=True, max_length=500, null=True)),
                ('vchr_delete_remark', models.CharField(blank=True, max_length=500, null=True)),
                ('dbl_total_amt', models.FloatField(blank=True, null=True)),
                ('dbl_total_tax', models.FloatField(blank=True, null=True)),
                ('json_tax', django.contrib.postgres.fields.jsonb.JSONField()),
                ('dbl_discount', models.FloatField(blank=True, null=True)),
                ('dbl_loyalty', models.FloatField(blank=True, null=True)),
                ('dbl_buyback', models.FloatField(blank=True, null=True)),
                ('dbl_supplier_amount', models.FloatField(blank=True, null=True)),
                ('dbl_coupon_amt', models.FloatField(blank=True, null=True)),
                ('int_doc_status', models.IntegerField(blank=True, null=True)),
                ('dat_created', models.DateTimeField(blank=True, null=True)),
                ('dat_updated', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'sales_master',
            },
        ),
    ]

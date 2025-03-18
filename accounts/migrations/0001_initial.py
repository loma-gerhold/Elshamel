# Generated by Django 5.1.6 on 2025-03-02 21:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Account Type Name')),
                ('code', models.CharField(max_length=2, verbose_name='Type Code')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Account Type',
                'verbose_name_plural': 'Account Types',
            },
        ),
        migrations.CreateModel(
            name='FiscalYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Fiscal Year')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('is_closed', models.BooleanField(default=False, verbose_name='Closed')),
                ('notes', models.TextField(blank=True, verbose_name='Notes')),
            ],
            options={
                'verbose_name': 'Fiscal Year',
                'verbose_name_plural': 'Fiscal Years',
                'ordering': ['-start_date'],
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='Account Code')),
                ('name', models.CharField(max_length=100, verbose_name='Account Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Current Balance')),
                ('normal_balance', models.CharField(choices=[('debit', 'Debit'), ('credit', 'Credit')], max_length=6, verbose_name='Normal Balance')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='accounts.account')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='accounts', to='accounts.accounttype')),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='FinancialStatement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('balance_sheet', 'Balance Sheet'), ('income_statement', 'Income Statement'), ('cash_flow', 'Cash Flow Statement')], max_length=20, verbose_name='Statement Type')),
                ('date', models.DateField(verbose_name='Statement Date')),
                ('data', models.JSONField(verbose_name='Statement Data')),
                ('generated_at', models.DateTimeField(auto_now_add=True, verbose_name='Generated At')),
                ('notes', models.TextField(blank=True, verbose_name='Notes')),
                ('generated_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('fiscal_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statements', to='accounts.fiscalyear')),
            ],
            options={
                'verbose_name': 'Financial Statement',
                'verbose_name_plural': 'Financial Statements',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Entry Date')),
                ('entry_type', models.CharField(choices=[('debit', 'Debit'), ('credit', 'Credit')], max_length=6, verbose_name='Entry Type')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Amount')),
                ('description', models.TextField(verbose_name='Description')),
                ('reference', models.CharField(max_length=50, verbose_name='Reference')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='journal_entries', to='accounts.account')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='journal_entries', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Journal Entry',
                'verbose_name_plural': 'Journal Entries',
                'ordering': ['-date', '-created_at'],
            },
        ),
    ]

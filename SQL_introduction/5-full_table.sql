--sql
#!/bin/bash

# Verilənlər bazası adı
DB_NAME="$1"

# SQL faylını oxu və MySQL serverinə göndər
cat 5-full_table.sql | mysql -hlocalhost -uroot -proot $DB_NAME | \
grep -v 'Using a password' | \
sed 's/\\n/\n/g' | \
sed 's/ //g' | \
sed 's/\t//g' | \
grep 'first_table' | \
grep 'AUTO_INCREMENT' | \
grep 'varchar' | \
grep 'char(1)' | \
grep 'created_at' | \
grep 'PRIMARY' | \
grep 'ENGINE' > table_desc

# Nəticəni yoxlamaq üçün
cat table_desc

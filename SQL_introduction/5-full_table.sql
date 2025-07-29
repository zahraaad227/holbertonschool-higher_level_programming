--sql
#!/bin/bash

# Verilənlər bazasının adı parametrlə qəbul edilir
DB_NAME="$1"

# SQL faylını oxuyub MySQL serverinə göndəririk və nəticəni manipulyasiya edirik
cat 5-full_table.sql | mysql -hlocalhost -uroot -proot $DB_NAME 2>&1 | \
grep -v 'Using a password' | \
# Yeni sətirləri düzəldirik
sed 's/\\n/\n/g' | \
# Bütün boşluqları çıxarırıq
sed 's/ //g' | \
# Tabulatorları çıxarırıq
sed 's/\t//g' | \
# Cədvəli tapırıq
grep 'first_table' | \
# AUTO_INCREMENT sətirini tapırıq
grep 'AUTO_INCREMENT' | \
# VARCHAR tipini tapırıq
grep 'varchar' | \
# CHAR(1) tipini tapırıq
grep 'char(1)' | \
# created_at sətirini tapırıq
grep 'created_at' | \
# PRIMARY KEY sətirini tapırıq
grep 'PRIMARY' | \
# ENGINE məlumatını tapırıq
grep 'ENGINE' > table_desc

# Nəticəni ekrana göstəririk
cat table_desc

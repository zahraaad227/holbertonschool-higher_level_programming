--sql
#!/bin/bash

# Verilənlər bazası adı
DB_NAME="$1"

# SQL faylını oxuyub MySQL serverinə göndəririk
cat 5-full_table.sql | mysql -hlocalhost -uroot -proot $DB_NAME | \
grep -v 'Using a password' | \
# Yeni sətirləri əvəz edin
sed 's/\\n/\n/g' | \
# Bütün boşluqları çıxarın
sed 's/ //g' | \
# Tabulatorları çıxarın
sed 's/\t//g' | \
# `first_table` ilə başlayan cədvəli tapın
grep 'first_table' | \
# AUTO_INCREMENT olan sətirləri tapın
grep 'AUTO_INCREMENT' | \
# VARCHAR tipi olan sətirləri tapın
grep 'varchar' | \
# CHAR(1) tipi olan sətirləri tapın
grep 'char(1)' | \
# created_at sütununu tapın
grep 'created_at' | \
# PRIMARY KEY açarını tapın
grep 'PRIMARY' | \
# ENGINE açarını tapın
grep 'ENGINE' > table_desc

# Nəticəni ekranda göstərin
cat table_desc

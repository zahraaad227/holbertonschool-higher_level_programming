--sql
DB_NAME="$1"
cat 5-full_table.sql | mysql -hlocalhost -uroot -p $DB_NAME

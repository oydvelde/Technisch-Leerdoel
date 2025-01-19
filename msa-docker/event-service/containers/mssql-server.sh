# shellcheck disable=SC1114
#!/bin/bash
sleep 10

# Start MSSQL Server en maak de database 'EventService-DB' met testdata aan als deze nog niet bestaat
i=0
gestart="false"

while [ "$gestart" = "false" ] && [ $i -le 20 ]; do
    echo ""
    echo "$i - Controleren of database 'EventService-DB' al bestaat"
    echo "-------------------------------------------------------"
    RESULT=$(/opt/mssql-tools18/bin/sqlcmd -S localhost -U sa -P "$SA_PASSWORD" -Q "IF DB_ID('EventService-DB') IS NOT NULL print 'YES'" -C)
    CODE=$?
    if [ "$RESULT" = "YES" ]; then
          gestart="true";
        echo ""
        echo "$i - Database 'EventService-DB' bestaat"
        echo "-------------------------------------"

    elif [ $CODE -eq 0 ] && [ "$RESULT" = "" ]; then
        echo ""
        echo "$i - Server beschikbaar, database 'EventService-DB' creeeren"
        echo "----------------------------------------------------------"

        /opt/mssql-tools18/bin/sqlcmd -S localhost -U sa -P "$SA_PASSWORD" -d master -i ./sql/ddl-script.sql -C

        if ls ./sql/constraints/*.sql; then
            echo ""
            echo "$i - Constraints toevoegen"
            echo "------------------------"

            for sqlfile in ./sql/constraints/*.sql; do
                echo "$i - $sqlfile"
                /opt/mssql-tools18/bin/sqlcmd -S localhost -U sa -P "$SA_PASSWORD" -d master -i $sqlfile -C
            done
        fi

        echo ""
        echo "$i - Testdata inserten"
        echo "----------------------"

        /opt/mssql-tools18/bin/sqlcmd -S localhost -U sa -P "$SA_PASSWORD" -d master -i ./sql/inserts.sql -C

    else
        echo ""
        echo "$i - Server nog niet beschikbaar"
        echo "--------------------------------"
        sleep 5
    fi
    i=$((i + 1))
done &
/opt/mssql/bin/sqlservr

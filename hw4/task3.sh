#!/bin/bash

gawk -F, 'BEGIN { count = 0; sum_age = 0; }

    # Check for passengers in 2nd class and embarked at Southampton
    $3 == 2 && substr($13, 1, 1) == "S" {

        # Replace male/female with M/F
        gsub(/female/, "F", $6);
        gsub(/male/, "M", $6);
        
        # Check if age is valid number
        if ($7 != "") {
            sum_age += $7;
            count++;
        }

        # Print the selected rows
        print $0
    }

    # Calculate average age and print after processing all records
    END {
        avg_age = (count > 0) ? sum_age / count : "N/A";
        print "Average Age:", avg_age;
    }
' titanic.csv

# since this is a modularized program, this code will need to import the overheads, cash on hand and profit loss python files,
# and this program will run the codes.
import overheads,cash_on_hand,profit_loss
from pathlib import Path

# This defines the location of where the exported text file will be, which is in the same folder as the program,
# and stores the path in a separate 'txt_export' variable.
txt_export=Path.cwd()/"summary_report.txt"

# Then, the program will run the overhead_check,cash_calc and profit_calc functions from the overheads, cash_on_hand
# and profit_loss python files, storing it in the overhead_export, coh_export and profit_export variables respectively.
overhead_export=overheads.overhead_check()
coh_export=cash_on_hand.cash_calc()
profit_export=profit_loss.profit_calc()

# The program will edit the text file with the data stored in the overhead_export, coh_export and profit_export variables.
# With the summary_report text file open in write mode,
with txt_export.open(mode="w") as file:
    # the program will write the data in the variables into the text file.
    file.write(f'{overhead_export}{coh_export}{profit_export}')
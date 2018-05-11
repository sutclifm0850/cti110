#Test Average and Grade
#April 22, 2018
#CTI 110 0901
#Sutcliffe

def calc_average( score1, score2, scoree3, score4, score5 ):
    average = ( score1 + score2 + score3 + score4 + score5 ) / 5
    return average

def determine_grade( userScore ):
    if ( userScore < 60 ):
        return "F"
    elif( userScore < 70 ):
        return "D"
    elif( userScore < 80 ):
        return "C"
    elif( userScore < 90 ):
        return "B"
    elif( userScore <= 100 ):
        return "A"

def ask_Score():
    score1 = float( input( 'Please enter first score: ' ))
    score2 = float( input( 'Please enter second score: ' ))
    score3 = float( input( 'Please enter third score: ' ))
    score4 = float( input( 'Please enter fourth score: ' ))
    score5 = float( input( 'Please enter fifth score: ' ))
    return score1,  score2, score3, score4, score5

def print_results(score1,  score2, score3, score4, score5 ):
    print( 'Score\tLetter Grade' )
    print( str(score1 ) + '\t' + determine_grade( score1 ),\
           str(score2 ) + '\t' + determine_grade( score2 ),\
           str(score3 ) + '\t' + determine_grade( score3 ),\
           str(score4 ) + '\t' + determine_grade( score4 ),\
           str(score5 ) + '\t' + determine_grade( score5 ), sep = '\n' )

def main():
    score1,  score2, score3, score4, score5 = ask_Score()
    print_results (score1, score2, score3, score4, score5 )

main()

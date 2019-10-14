a = input()

onesplace = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}

tensplace = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']


def number(Number):
    if 1 <= Number < 19:
        return onesplace[Number]
    elif 20 <= Number <= 99:
        tens, below_ten = divmod(Number, 10)
        return tensplace[tens - 2] + ' ' + onesplace[below_ten]
    else:
        print("Number out of range")
    print()




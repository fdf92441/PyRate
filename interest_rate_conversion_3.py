from tkinter import *


def type_handling(interest_rate, type_rate, target_rate):
    if type_rate == 'EA':
        EA(interest_rate, target_rate)
    elif type_rate == 'ASV':
        SV = interest_rate / 2
        basic_EA = float((1 + SV)**(2) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'ASA':
        SA = interest_rate / 2
        basic_EA = float((1 - SA)**(-2) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'ACV':
        CV = interest_rate / 3
        basic_EA = float((1 + CV)**(3) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'ACA':
        CA = interest_rate / 3
        basic_EA = float((1 - CA)**(-3) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'ATV':
        TV = interest_rate / 4
        basic_EA = float((1 + TV)**(4) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'ATA':
        TA = interest_rate / 4
        basic_EA = float((1 - TA)**(-4) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'ABV':
        BV = interest_rate / 6
        basic_EA = float((1 + BV)**(6) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'ABA':
        BA = interest_rate / 6
        basic_EA = float((1 - BA)**(-6) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'AMV':
        MV = interest_rate / 12
        basic_EA = float((1 + MV)**(12) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'AMA':
        MA = interest_rate / 12
        basic_EA = float((1 - MA)**(-12) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'AQV':
        QV = interest_rate / 24
        basic_EA = float((1 + QV)**(24) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'AQA':
        QA = interest_rate / 24
        basic_EA = float((1 - QA)**(-24) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'ADV':
        DV = interest_rate / 365
        basic_EA = float((1 + DV)**(365) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'ADA':
        DA = interest_rate / 365
        basic_EA = float((1 - QA)**(-365) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'SCV':
        CV = interest_rate / (6 / 4)
        basic_EA = float((1 + CV)**(3) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'SCA':
        CA = interest_rate / (6 / 4)
        basic_EA = float((1 - CA)**(-3) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'STV':
        TV = interest_rate / (6 / 3)
        basic_EA = float((1 + TV)**(4) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'STA':
        TA = interest_rate / (6 / 3)
        basic_EA = float((1 - TA)**(-4) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'SBV':
        BV = interest_rate / (6 / 2)
        basic_EA = float((1 + BV)**(6) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'SBA':
        BA = interest_rate / (6 / 2)
        basic_EA = float((1 - BA)**(-6) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'SMV':
        MV = interest_rate / (6 / 1)
        basic_EA = float((1 + MV)**(12) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'SMA':
        MA = interest_rate / (6 / 1)
        basic_EA = float((1 - MA)**(-12) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'SQV':
        QV = interest_rate / (6 / 0.5)
        basic_EA = float((1 + QV)**(24) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'SQA':
        MA = interest_rate / (6 / 0.5)
        basic_EA = float((1 - QA)**(-24) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'SDV':
        DV = interest_rate / (365 / 2)
        basic_EA = float((1 + DV)**(365) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'SDA':
        DA = interest_rate / (365 / 2)
        basic_EA = float((1 - DA)**(-365) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'CTV':
        TV = interest_rate / (4 / 3)
        basic_EA = float((1 + TV)**(4) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'CTA':
        TA = interest_rate / (4 / 3)
        basic_EA = float((1 - TA)**(-4) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'CBV':
        BV = interest_rate / (4 / 2)
        basic_EA = float((1 + BV)**(6) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'CBA':
        BA = interest_rate / (4 / 2)
        basic_EA = float((1 - BA)**(-6) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'CMV':
        MV = interest_rate / (4 / 1)
        basic_EA = float((1 + MV)**(12) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'CMA':
        MA = interest_rate / (4 / 1)
        basic_EA = float((1 - MA)**(-12) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'CQV':
        QV = interest_rate / (4 / 0.5)
        basic_EA = float((1 + MV)**(24) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'CQA':
        QA = interest_rate / (4 / 0.5)
        basic_EA = float((1 - QA)**(-24) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'CDV':
        DV = interest_rate / (365 / 3)
        basic_EA = float((1 + DV)**(365) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'CDA':
        DA = interest_rate / (365 / 3)
        basic_EA = float((1 - DA)**(-365) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'TBV':
        BV = interest_rate / (3 / 2)
        basic_EA = float((1 + BV)**(6) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'TBA':
        BA = interest_rate / (3 / 2)
        basic_EA = float((1 - BA)**(-6) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'TMV':
        MV = interest_rate / (3 / 1)
        basic_EA = float((1 + MV)**(12) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'TMA':
        MA = interest_rate / (3 / 1)
        basic_EA = float((1 - MA)**(-12) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'TQV':
        QV = interest_rate / (3 / 0.5)
        basic_EA = float((1 + QV)**(24) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'TQA':
        QA = interest_rate / (3 / 0.5)
        basic_EA = float((1 - QA)**(-24) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'TDV':
        DV = interest_rate / (365 / 4)
        basic_EA = float((1 + DV)**(365) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'TDA':
        DA = interest_rate / (365 / 4)
        basic_EA = float((1 - DA)**(-365) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'BMV':
        MV = interest_rate / (2 / 1)
        basic_EA = float((1 + MV)**(12) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'BMA':
        MA = interest_rate / (2 / 1)
        basic_EA = float((1 - MA)**(-12) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'BQV':
        QV = interest_rate / (2 / 0.5)
        basic_EA = float((1 + QV)**(24) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'BQA':
        QA = interest_rate / (2 / 0.5)
        basic_EA = float((1 - QA)**(-24) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'BDV':
        DV = interest_rate / (365 / 6)
        basic_EA = float((1 + DV)**(365) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'BDA':
        DA = interest_rate / (365 / 6)
        basic_EA = float((1 - DA)**(-365) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'MQV':
        QV = interest_rate / (1 / 0.5)
        basic_EA = float((1 + QV)**(24) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'MQA':
        QA = interest_rate / (1 / 0.5)
        basic_EA = float((1 - QA)**(-24) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'MDV':
        DV = interest_rate / (365 / 12)
        basic_EA = float((1 + DV)**(365) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'MDA':
        DA = interest_rate / (365 / 12)
        basic_EA = float((1 - DA)**(-365) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'SV':
        basic_EA = float((1 + interest_rate)**(2) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'SA':
        basic_EA = float((1 - interest_rate)**(-2) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'CV':
        basic_EA = float((1 + interest_rate)**(3) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'CA':
        basic_EA = float((1 - interest_rate)**(-3) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'TV':
        basic_EA = float((1 + interest_rate)**(4) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'TA':
        basic_EA = float((1 - interest_rate)**(-4) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'BV':
        basic_EA = float((1 + interest_rate)**(6) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'BA':
        basic_EA = float((1 - interest_rate)**(-6) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'MV':
        basic_EA = float((1 + interest_rate)**(12) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'MA':
        basic_EA = float((1 - interest_rate)**(-12) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'QV':
        basic_EA = float((1 + interest_rate)**(24) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'QA':
        basic_EA = float((1 - interest_rate)**(-24) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'DV':
        basic_EA = float((1 + interest_rate)**(365) - 1)
        EA(basic_EA, target_rate)
    elif type_rate == 'DA':
        basic_EA = float((1 - interest_rate)**(-365) - 1)
        EA(basic_EA, target_rate)
    else:
        menssage()


def EA(interest_rate, target_rate):
    if target_rate == 'ASV':
        SV = float((1 + interest_rate)**(1 / 2) - 1)
        ASV = SV * 2
        print_new_rate(ASV, target_rate)

    elif target_rate == 'ASA':
        SA = float((1 + interest_rate)**(-1 / 2) - 1) * -1
        ASA = SA * 2
        print_new_rate(ASA, target_rate)

    elif target_rate == 'ACV':
        CV = float((1 + interest_rate)**(1 / 3) - 1)
        ACV = CV * 3
        print_new_rate(ACV, target_rate)

    elif target_rate == 'ACA':
        CA = float((1 + interest_rate)**(-1 / 3) - 1) * -1
        ACA = CA * 3
        print_new_rate(ACA, target_rate)

    elif target_rate == 'ATV':
        TV = float((1 + interest_rate)**(1 / 4) - 1)
        ATV = TV * 4
        print_new_rate(ATV, target_rate)

    elif target_rate == 'ATA':
        TA = float((1 + interest_rate)**(-1 / 4) - 1) * -1
        ATA = TA * 4
        print_new_rate(ATA, target_rate)

    elif target_rate == 'ABV':
        BV = float((1 + interest_rate)**(1 / 6) - 1)
        ABV = BV * 6
        print_new_rate(ABV, target_rate)

    elif target_rate == 'ABA':
        BA = float((1 + interest_rate)**(-1 / 6) - 1) * -1
        ABA = BA * 6
        print_new_rate(ABA, target_rate)

    elif target_rate == 'AMV':
        MV = float((1 + interest_rate)**(1 / 12) - 1)
        AMV = MV * 12
        print_new_rate(AMV, target_rate)

    elif target_rate == 'AMA':
        MA = float((1 + interest_rate)**(-1 / 12) - 1) * -1
        AMA = MA * 12
        print_new_rate(AMA, target_rate)

    elif target_rate == 'AQV':
        QV = float((1 + interest_rate)**(1 / 24) - 1)
        AQV = QV * 24
        print_new_rate(AQV, target_rate)

    elif target_rate == 'AQA':
        QA = float((1 + interest_rate)**(-1 / 24) - 1) * -1
        AQA = QA * 24
        print_new_rate(AQA, target_rate)

    elif target_rate == 'ADV':
        DV = float((1 + interest_rate)**(1 / 365) - 1)
        ADV = DV * 365
        print_new_rate(ADV, target_rate)

    elif target_rate == 'ADA':
        DA = float((1 + interest_rate)**(-1 / 365) - 1) * -1
        ADA = DA * 365
        print_new_rate(ADA, target_rate)

    elif target_rate == 'SCV':
        CV = float((1 + interest_rate)**(1 / 3) - 1)
        SCV = CV * (6 / 4)
        print_new_rate(SCV, target_rate)

    elif target_rate == 'SCA':
        CA = float((1 + interest_rate)**(-1 / 3) - 1) * -1
        SCA = CA * (6 / 4)
        print_new_rate(SCA, target_rate)

    elif target_rate == 'STV':
        TV = float((1 + interest_rate)**(1 / 4) - 1)
        STV = TV * (6 / 3)
        print_new_rate(STV, target_rate)

    elif target_rate == 'STA':
        TA = float((1 + interest_rate)**(-1 / 4) - 1) * -1
        STA = TA * (6 / 3)
        print_new_rate(STA, target_rate)

    elif target_rate == 'SBV':
        BV = float((1 + interest_rate)**(1 / 6) - 1)
        SBV = BV * (6 / 2)
        print_new_rate(SBV, target_rate)

    elif target_rate == 'SBA':
        BA = float((1 + interest_rate)**(-1 / 6) - 1) * -1
        SBA = BA * (6 / 2)
        print_new_rate(SBA, target_rate)

    elif target_rate == 'SMV':
        MV = float((1 + interest_rate)**(1 / 12) - 1)
        SMV = MV * (6 / 1)
        print_new_rate(SMV, target_rate)

    elif target_rate == 'SMA':
        MA = float((1 + interest_rate)**(-1 / 12) - 1) * -1
        SMA = MA * (6 / 1)
        print_new_rate(SMA, target_rate)

    elif target_rate == 'SQV':
        QV = float((1 + interest_rate)**(1 / 24) - 1)
        SQV = QV * 12
        print_new_rate(SQV, target_rate)

    elif target_rate == 'SQA':
        QA = float((1 + interest_rate)**(-1 / 24) - 1) * -1
        SQA = QA * 12
        print_new_rate(SQA, target_rate)

    elif target_rate == 'SDV':
        DV = float((1 + interest_rate)**(1 / 365) - 1)
        SDV = DV * (365 / 2)
        print_new_rate(SDV, target_rate)

    elif target_rate == 'SDA':
        DA = float((1 + interest_rate)**(-1 / 365) - 1) * -1
        SDA = DA * (365 / 2)
        print_new_rate(SDA, target_rate)

    elif target_rate == 'CTV':
        TV = float((1 + interest_rate)**(1 / 4) - 1)
        CTV = TV * (4 / 3)
        print_new_rate(CTV, target_rate)

    elif target_rate == 'CTA':
        TA = float((1 + interest_rate)**(-1 / 4) - 1) * -1
        CTA = TA * (4 / 3)
        print_new_rate(CTA, target_rate)

    elif target_rate == 'CBV':
        BV = float((1 + interest_rate)**(1 / 6) - 1)
        CBV = BV * (4 / 2)
        print_new_rate(CBV, target_rate)

    elif target_rate == 'CBA':
        BA = float((1 + interest_rate)**(-1 / 6) - 1) * -1
        CBA = BA * (4 / 2)
        print_new_rate(CBA, target_rate)

    elif target_rate == 'CMV':
        MV = float((1 + interest_rate)**(1 / 12) - 1)
        CMV = MV * (4 / 1)
        print_new_rate(CMV, target_rate)

    elif target_rate == 'CMA':
        MA = float((1 + interest_rate)**(-1 / 12) - 1) * -1
        CMA = MA * (4 / 1)
        print_new_rate(CMA, target_rate)

    elif target_rate == 'CQV':
        QV = float((1 + interest_rate)**(1 / 24) - 1)
        CQV = QV * 8
        print_new_rate(CQV, target_rate)

    elif target_rate == 'CQA':
        QA = float((1 + interest_rate)**(-1 / 24) - 1) * -1
        CQA = QA * 8
        print_new_rate(CQA, target_rate)

    elif target_rate == 'CDV':
        DV = float((1 + interest_rate)**(1 / 365) - 1)
        CDV = DV * (365 / 3)
        print_new_rate(CDV, target_rate)

    elif target_rate == 'CDA':
        DA = float((1 + interest_rate)**(-1 / 365) - 1) * -1
        CDA = DA * (365 / 3)
        print_new_rate(CDA, target_rate)

    elif target_rate == 'TBV':
        BV = float((1 + interest_rate)**(1 / 6) - 1)
        TBV = MV * (3 / 2)
        print_new_rate(TBV, target_rate)

    elif target_rate == 'TBA':
        BA = float((1 + interest_rate)**(-1 / 6) - 1) * -1
        TBA = BA * (3 / 2)
        print_new_rate(TBA, target_rate)

    elif target_rate == 'TMV':
        MV = float((1 + interest_rate)**(1 / 12) - 1)
        TMV = MV * (3 / 1)
        print_new_rate(TMV, target_rate)

    elif target_rate == 'TMA':
        MA = float((1 + interest_rate)**(-1 / 12) - 1) * -1
        TMA = MA * (3 / 1)
        print_new_rate(TMA, target_rate)

    elif target_rate == 'TQV':
        QV = float((1 + interest_rate)**(1 / 24) - 1)
        TQV = QV * 6
        print_new_rate(TQV, target_rate)

    elif target_rate == 'TQA':
        QA = float((1 + interest_rate)**(-1 / 24) - 1) * -1
        TQA = QA * 6
        print_new_rate(TQA, target_rate)

    elif target_rate == 'TDV':
        DV = float((1 + interest_rate)**(1 / 365) - 1)
        TDV = DV * (365 / 4)
        print_new_rate(TDV, target_rate)

    elif target_rate == 'TDA':
        DA = float((1 + interest_rate)**(-1 / 365) - 1) * -1
        TDA = DA * (365 / 4)
        print_new_rate(TDA, target_rate)

    elif target_rate == 'BMV':
        MV = float((1 + interest_rate)**(1 / 12) - 1)
        BMV = MV * (2 / 1)
        print_new_rate(BMV, target_rate)

    elif target_rate == 'BMA':
        MA = float((1 + interest_rate)**(-1 / 12) - 1) * -1
        BMA = MA * (2 / 1)
        print_new_rate(BMA, target_rate)

    elif target_rate == 'BQV':
        QV = float((1 + interest_rate)**(1 / 24) - 1)
        BQV = QV * 4
        print_new_rate(BQV, target_rate)

    elif target_rate == 'BQA':
        QA = float((1 + interest_rate)**(-1 / 24) - 1) * -1
        BQA = QA * 4
        print_new_rate(BQA, target_rate)

    elif target_rate == 'BDV':
        DV = float((1 + interest_rate)**(1 / 365) - 1)
        BDV = DV * (365 / 6)
        print_new_rate(BDV, target_rate)

    elif target_rate == 'BDA':
        DA = float((1 + interest_rate)**(-1 / 365) - 1) * -1
        BDA = DA * (365 / 6)
        print_new_rate(BDA, target_rate)

    elif target_rate == 'MQV':
        QV = float((1 + interest_rate)**(1 / 24) - 1)
        MQV = QV * 2
        print_new_rate(MQV, target_rate)

    elif target_rate == 'MQA':
        QA = float((1 + interest_rate)**(-1 / 24) - 1) * -1
        MQA = QA * 2
        print_new_rate(MQA, target_rate)

    elif target_rate == 'MDV':
        DV = float((1 + interest_rate)**(1 / 365) - 1)
        MDV = DV * (365 / 12)
        print_new_rate(MDV, target_rate)

    elif target_rate == 'MDA':
        DA = float((1 + interest_rate)**(-1 / 365) - 1) * -1
        MDA = DA * (365 / 12)
        print_new_rate(MDA, target_rate)

    elif target_rate == 'SV':
        SV = float((1 + interest_rate)**(1 / 2) - 1)
        print_new_rate(SV, target_rate)

    elif target_rate == 'SA':
        SA = float((1 + interest_rate)**(-1 / 2) - 1) * -1
        print_new_rate(SA, target_rate)

    elif target_rate == 'CV':
        CV = float((1 + interest_rate)**(1 / 3) - 1)
        print_new_rate(CV, target_rate)

    elif target_rate == 'CA':
        CA = float((1 + interest_rate)**(-1 / 3) - 1) * -1
        print_new_rate(CA, target_rate)

    elif target_rate == 'TV':
        TV = float((1 + interest_rate)**(1 / 4) - 1)
        print_new_rate(TV, target_rate)

    elif target_rate == 'TA':
        TA = float((1 + interest_rate)**(-1 / 4) - 1) * -1
        print_new_rate(TA, target_rate)

    elif target_rate == 'BV':
        BV = float((1 + interest_rate)**(1 / 6) - 1)
        print_new_rate(BV, target_rate)

    elif target_rate == 'BA':
        BA = float((1 + interest_rate)**(-1 / 6) - 1) * -1
        print_new_rate(BA, target_rate)

    elif target_rate == 'MV':
        MV = float((1 + interest_rate)**(1 / 12) - 1)
        print_new_rate(MV, target_rate)

    elif target_rate == 'MA':
        MA = float((1 + interest_rate)**(-1 / 12) - 1) * -1
        print_new_rate(MA, target_rate)

    elif target_rate == 'QV':
        QV = float((1 + interest_rate)**(1 / 24) - 1)
        print_new_rate(QV, target_rate)

    elif target_rate == 'QA':
        QA = float((1 + interest_rate)**(-1 / 24) - 1) * -1
        print_new_rate(QA, target_rate)

    elif target_rate == 'DV':
        DV = float((1 + interest_rate)**(1 / 365) - 1)
        print_new_rate(DV, target_rate)

    elif target_rate == 'DA':
        DA = float((1 + interest_rate)**(-1 / 365) - 1) * -1
        print_new_rate(DA, target_rate)

    elif target_rate == 'EA':
        print_new_rate(interest_rate, target_rate)

    else:
        menssage()


def print_new_rate(new_rate, target_rate):
    new_rate2 = new_rate * 100
    numeroPantalla.set('{}% {}'.format(new_rate2, target_rate))


def menssage():
    numeroPantalla.set('No se ingreso un valor correcto')


def conversion():
    try:
        interest_rate_2 = rate.get()
        interest_rate = float(interest_rate_2) / 100
        type_rate = str(type1.get().upper())
        target_rate = str(type2.get().upper())
        type_handling(interest_rate, type_rate, target_rate)
    except:
        menssage()


def inforamcion():
    root2 = Tk()
    root2.title('Inforamción')
    #root2.geometry('500x500')

    creado = Label(root2, text='TIPOS DE TASA DE INTERÉS')
    creado.grid(row=0, column=0, padx=5, pady=5)
    creado.config(font='Helvetica 15 bold')

    tutorial = Label(root2,
                     text='''
    EA = Efectivo Anual
    ASV = Anual Semestre Vencido
    ASA = Anual Semestre Anticipado
    ACV = Anual Cuatrimestre Vencido
    ACA = Anual Cuatrimestre Anticipado
    ATV = Anual Trimestre Vencido
    ATA = Anual Trimestre Anticipado
    ABV = Anual Bimestre Vencido
    ABA = Anual Bimestre Anticipado
    AMV = Anual Mes Vencido
    AMA = Anual Mes Anticipado
    AQV = Anual Quincena Vencida
    AQA = Anual Quincena Anticipada
    ADV = Anual Diaria Vencida
    ADA = Anual Diaria Anticipada
    SCV = Semestral Cuatrimestre Vencido
    SCA = Semestral Cuatrimestre Anticipado
    STV = Semestral Trimestre Vencido
    STA = Semestral Trimestre Anticipado
    SBV = Semestral Bimestre Vencido
    SBA = Semestral Bimestre Anticipado
    SMV = Semestral Mes Vencido
    SMA = Semestral Mes Anticipado
    SQV = Semestral Quincena Vencida
    SQA = Semestral Quincena Anticipada
    SDV = Semestral Diaria Vencida
    SDA = Semestral Diaria Anticipada
    CTV = Cuatrimestral Trimestre Vencido
    CTA = Cuatrimestral Trimestre Anticipado
    CBV = Cuatrimestral Bimestre Vencido
    CBA = Cuatrimestral Bimestre Anticipado
    CMV = Cuatrimestral Mes Vencido
    CMA = Cuatrimestral Mes Anticipado
    CQV = Cuatrimestral Quincena Vencida
    CQA = Cuatrimestral Quincena Anticipada
    CDV = Cuatrimestral Diaria Vencida
    CDA = Cuatrimestral Diaria Anticipada
    ''')
    tutorial.grid(row=1, column=0, padx=5, pady=5)
    tutorial.config(font='Helvetica 12')

    tutorial2 = Label(root2,
                     text='''
    TBV = Trimestral Bimestre Vencido
    TBA = Trimestral Bimestre Anticipado
    TMV = Trimestral Mes Vencido
    TMA = Trimestral Mes Anticipado
    TQV = Trimestral Quincena Vencida
    TQA = Trimestral Quincena Anticipada
    TDV = Trimestral Diaria Vencida
    TDA = Trimestral Diaria Anticipada
    BMV = Bimestral Mes Vencido
    BMA = Bimestral Mes Anticipado
    BQV = Bimestral Quincena Vencida
    BQA = Bimestral Quincena Anticipada
    BDV = Bimestral Diaria Vencida
    BDA = Bimestral Diaria Anticipada
    MQV = Mensual Quincena Vencida
    MQA = Mensual Quincena Anticipada
    MDV = Mensual Diaria Vencida
    MDA = Mensual Diaria Anticipada
    SV = Semestre Vencido
    SA = Semestre Anticipado
    CV = Cuatrimestre Vencido
    CA = Cuatrimestre Anticipado
    TV = Trimestral Vencido
    TA = Trimestral Anticipado
    BV = Bimestral Vencido
    BA = Bimestral Anticipado
    MV = Mes Vencido
    MA = Mes Anticipado
    QV = Quincena Vencida
    QA = Quincena Anticipada
    DV = Diaria Vencida
    DA = Diaria Anticipada

    Creado por Daniel Franco
    fdf92444@gmail.com
    ''')
    tutorial2.grid(row=1, column=1, padx=5, pady=5)
    tutorial2.config(font='Helvetica 12')

    root2.mainloop()


if __name__ == "__main__":
    root = Tk()
    root.title('Convertidor de tasas de interés')
    root.resizable(0, 0)
    try:
        root.iconbitmap('lente.ico')
    except:
        pass

    frame_principal = Frame(root)
    frame_principal.pack()
    #frame_principal.config(bg='grey')

    rate = StringVar()
    type1 = StringVar()
    type2 = StringVar()
    numeroPantalla = StringVar()

    pantalla = Entry(frame_principal,
                     state="disabled",
                     width=60,
                     textvariable=numeroPantalla)
    pantalla.grid(row=0, column=0, columnspan=5, padx=5, pady=5)
    pantalla.config(justify='center', font=15, fg='black')

    textTasa = Label(frame_principal, text='Ingrese la Tasa:')
    textTasa.grid(row=1, column=0, padx=5, pady=5)

    numberTasa = Entry(frame_principal, textvariable=rate)
    numberTasa.grid(row=1, column=1, padx=5, pady=5)

    porcentaje = Label(frame_principal, text='%')
    porcentaje.grid(row=1, column=2, padx=0, pady=5, sticky='w')

    textTipo = Label(frame_principal, text='Tipo:')
    textTipo.grid(row=1, column=3, padx=5, pady=5)
    numberTipo = Entry(frame_principal, textvariable=type1)
    numberTipo.grid(row=1, column=4, padx=5, pady=5)

    textNewTipo = Label(frame_principal, text='Tipo a convertir:')
    textNewTipo.grid(row=2, column=0, padx=5, pady=5)
    numberNewTipo = Entry(frame_principal, textvariable=type2)
    numberNewTipo.grid(row=2, column=1, padx=5, pady=5)

    botonConvertir = Button(frame_principal,
                            text='Convertir',
                            width=25,
                            command=conversion)
    botonConvertir.grid(row=2, column=3, columnspan=4, padx=5, pady=5)

    botonInfo = Button(frame_principal, text='?', command=inforamcion)
    botonInfo.grid(row=0, column=5, padx=5, pady=5)

    root.mainloop()

# Por Daniel Alejandro Franco Meneses
# Versión 1.0 Se creo el cerebro de la conversión de tasas y se realizó varias pruebas para verificar su funcionamiento correcto.
# Versión 1.1 Se creo la interfaz gráfica.
# Versión 1.2 Se crea compatibilidad con mayúsculas y minúsculas.
# Version 1.3 Se ingresa soporte a la tasa Quincenal y Diaria.

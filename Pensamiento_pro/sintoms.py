def calc_symp(prior_a,p_b_dado_a, p_b):
    return prior_a * p_b_dado_a / p_b




if __name__ == "__main__":
    pro_cancer= 1/100000
    pro_symp_dado_cancer= 1
    pro_symp_dado_nocancer= 10/99999
    pro_no_tener_cancer= 1 - pro_cancer

    pro_symp= (pro_symp_dado_cancer* pro_cancer)+(pro_symp_dado_nocancer*pro_no_tener_cancer)
    pro_cancer_dado_symp= calc_symp(pro_cancer,pro_symp_dado_cancer,pro_symp)
    print(pro_cancer_dado_symp)

def detect_datatype(df):
    # detect columns in data frame to be numeric or category
    # col_numeric,col_category = detect_DF(df)
    
    row_num,col_num = df.shape
    col_names = df.columns
    
    if row_num<50:
        df_check = df
    else:
        df_check = df[:50]
    
    # refresh row_num for later use
    row_num = df_check[0]
    
    # list to store index
    idx_numeric = []
    idx_category = []

    for ii in range(col_num):
        
        catg_num = len(pd.unique(df_check[col_names[ii]]))
        
        if catg_num < row_num/3:
            idx_category.append(ii)
        else:
            idx_numeric.append(ii)
    
    col_numeric = col_names[idx_numeric]
    col_category = col_names[idx_category]
    
    return(col_numeric,col_category)


    # df_numeric = df[col_names[idx_numeric]]
    # df_category = df[col_names[idx_category]]
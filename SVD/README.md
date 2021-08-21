The purpose of this project is to create a least squares regression model using the Singular Value Decomposition (SVD).

This dataset cointains information from multiple processors of different brands. 

This machine learning model predicts the performance of a given CPU based on the following factors:
   1. vendor name: 30 
      (adviser, amdahl,apollo, basf, bti, burroughs, c.r.d, cambex, cdc, dec, 
       dg, formation, four-phase, gould, honeywell, hp, ibm, ipl, magnuson, 
       microdata, nas, ncr, nixdorf, perkin-elmer, prime, siemens, sperry, 
       sratus, wang)
   2. Model Name: many unique symbols
   3. MYCT: machine cycle time in nanoseconds (integer)
   4. MMIN: minimum main memory in kilobytes (integer)
   5. MMAX: maximum main memory in kilobytes (integer)
   6. CACH: cache memory in kilobytes (integer)
   7. CHMIN: minimum channels in units (integer)
   8. CHMAX: maximum channels in units (integer)
   9. PRP: published relative performance (integer)
  10. ERP: estimated relative performance from the original article (integer)

To prepare the data for this model, we dropped the columns ERP and Model Name. Then, we get dummy variables for the vendor names.Afterwards, we select our feature columns. Finally we pad a column of 1's on the matrix, this column allows our least square regression model to not be fixated to the origin.

Once the data is prepared, we divide the data into training and testing data. The model then executes the SVD function of NumPy.

Finally we visualize the performance of the model in matplotlib.

We can see that this model predicts performance to the decimal place of the actual performance.

Data source:
https://archive.ics.uci.edu/ml/datasets/Computer+Hardware



from rembg import remove
input_path="resim.jpg" #Resim burada olduğu direk adını yazdım.Farklı yerde olsaydı / uzantısı yazılmalıdır.
output_path="output.png"

with open(input_path,'rb') as i: #okunacak, i=input
    with open(output_path,'wb') as o: #yazılacak, o=output
         input_file=i.read()
         output_file=remove(input_file )
         o.write(output_file)

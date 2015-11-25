function [ A ] = read_file( input_args )
    fid = fopen(input_args, 'r');
    tline = fgetl(fid);
    %  Split header
    A(1,:) = regexp(tline, '\,', 'split');
    %  Parse and read rest of file
    ctr = 1;
    while(~feof(fid))
    if ischar(tline)    
          ctr = ctr + 1;
          tline = fgetl(fid);         
          A(ctr,:) = regexp(tline, '\,', 'split'); 
    else
          break;     
    end
    end
    fclose(fid);
end


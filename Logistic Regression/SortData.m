function [ sorted ] = SortData( raw_data )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
    [row, col] = size(raw_data);
    sorted = zeros(row,col);
    nameKey = cell(row, 1);
    marketKey = cell(row, 1);
    ix=cellfun('isempty',marketKey);
    marketKey(ix)={'-1'};
    marketCount = 1;
    
    regionKey = cell(row, 1);
    ix=cellfun('isempty',regionKey);
    regionKey(ix)={'-1'};
    regionCount = 1;
    
    for i = 1:row
        sorted(i,3) = str2num(raw_data{i,3});
        sorted(i,7) = str2num(raw_data{i,7});
        sorted(i,8) = str2num(raw_data{i,8});
        sorted(i,9) = str2num(raw_data{i,9});
        sorted(i,10) = str2num(raw_data{i,10});
        
        % name
        nameKey{i, 1} = raw_data(i,1);
        sorted(i, 1) = i;
        
        % market
        [idx,~] = ind2sub(size(marketKey), strmatch(raw_data(i,2), marketKey, 'exact'));
        
        if isempty(idx)
            sorted(i,2) = marketCount;
            marketKey(marketCount) = raw_data(i,2);
            marketCount = marketCount + 1;
        else
            sorted(i,2) = idx(1,1);
        end
        
        % status
        if strcmp(raw_data(i,4), 'closed')
            sorted(i,4) = 0;

        elseif strcmp(raw_data(i,4), 'operating')
            sorted(i,4) = 1;

        elseif strcmp(raw_data(i,4), 'acquired')
            sorted(i,4) = 1; 
        end

        % country
        sorted(i,5) = CountrySort(raw_data(i,5));
        
        % region
        [idx,~] = ind2sub(size(regionKey), strmatch(raw_data(i,6), regionKey, 'exact'));
        
        if isempty(idx)
            sorted(i,6) = regionCount;
            regionKey(regionCount) = raw_data(i,6);
            regionCount = regionCount + 1;
        else
            sorted(i,6) = idx(1,1);
        end
    end
end


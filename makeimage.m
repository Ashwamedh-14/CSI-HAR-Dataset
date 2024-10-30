% Base directory containing subdirectories of CSV files
base_dir = 'D:/CSI-HAR-Dataset/CSI-HAR-Dataset/';  % Adjust this to your folder

% Get a list of all subdirectories in the base folder
subdirs = dir(base_dir);
subdirs = subdirs([subdirs.isdir]);  % Keep only directories

% Loop over each subdirectory
for i = 1:length(subdirs)
    subdir_name = subdirs(i).name;
    
    % Skip '.' and '..' directories
    if strcmp(subdir_name, '.') || strcmp(subdir_name, '..')
        continue;
    end
    
    % Full path of the current subdirectory
    subdir_path = fullfile(base_dir, subdir_name);
    
    % Get all CSV files in the current subdirectory
    csv_files = dir(fullfile(subdir_path, '*.csv'));
    
    % Loop over each CSV file in the current subdirectory
    for j = 1:length(csv_files)
        csv_file_name = csv_files(j).name;
        
        % Skip files that have 'annotation' in their name
        if contains(csv_file_name, 'Annotation')
            continue;
        end
        
        % Full path to the CSV file
        csv_file_path = fullfile(subdir_path, csv_file_name);
        
        % Read the CSV data into a matrix
        M = csvread(csv_file_path);
        
        % Create the pseudocolor plot
        figure;
        pcolor(M);
        shading flat;  % Equivalent to 'shading flat' in MATLAB
        axis off;      % Turn off axis
        
        % Optional: Save the figure as a PNG image
        [~, name, ~] = fileparts(csv_file_path);  % Extract file name without extension
        saveas(gcf, fullfile(subdir_path, [name '.png']));  % Save as PNG
        
        close(gcf);  % Close the figure after saving
    end
end

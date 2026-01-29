source("a20_config/a20_config.R")


# Try to load pacman using require(), If it's not found, installs it from CRAN
if (!require("pacman")) install.packages("pacman")
library(pacman)
# Installs any missing packages and loads them
pacman::p_load(readxl, dplyr, ggplot2, svglite, ggrepel, writexl)


# deals count


deals_by_year <- read_excel(file$rt_sp070_20__vc_deals_by_year__xl)
deals_by_year

sum(deals_by_year$count)
colnames(deals_by_year)


plt_deals_count <- ggplot(deals_by_year, aes(x = deal_year, y = count)) +
    geom_bar(stat = "identity", fill = "#2E86AB", width = 0.7) +
    geom_text(aes(label = count), vjust = -0.5, size = 3.5, color = "#333333") +
    scale_x_continuous(breaks = deals_by_year$deal_year) +
    scale_y_continuous(expand = expansion(mult = c(0, 0.1))) +
    labs(title = "Number of Deals Over Time",
         subtitle = paste("Total deals:", sum(deals_by_year$count)),
         x = "Year",
         y = "Number of Deals") +
    theme_minimal(base_size = 12) +
    theme(
        plot.title = element_text(face = "bold", size = 16, margin = margin(b = 5)),
        plot.subtitle = element_text(size = 11, color = "#666666", margin = margin(b = 15)),
        plot.caption = element_text(size = 9, color = "#999999", hjust = 1),
        axis.title = element_text(face = "bold", size = 11),
        axis.text.x = element_text(angle = 45, hjust = 1, size = 10),
        axis.text.y = element_text(size = 10),
        panel.grid.major.x = element_blank(),
        panel.grid.minor = element_blank(),
        panel.grid.major.y = element_line(color = "#E0E0E0", linewidth = 0.3),
        plot.margin = margin(20, 20, 20, 20)
    )

ggsave(file$rp_sp090_05__deals_count_by_year__fmt1__pdf,
       plot = plt_deals_count,
       width = 12,
       height = 7,
       dpi = 300)

ggsave(file$rp_sp090_10__deals_count_by_year__fmt2__svg,
       plot = plt_deals_count,
       width = 12,
       height = 7,
       dpi = 300)



# Deals amount


df <- read_excel(file$dp_sp070_15__vc_related_deals__n2Final__xl)
nrow(df)

table(df$DealSizeStatus)

typeof(df$DealSize)


summary(df$DealSize)

stats <- df %>%
    summarise(
        Mean = mean(DealSize, na.rm = TRUE),
        Median = median(DealSize, na.rm = TRUE),
        SD = sd(DealSize, na.rm = TRUE),
        Min = min(DealSize, na.rm = TRUE),
        Max = max(DealSize, na.rm = TRUE),
        Count = n(),
        Missing = sum(is.na(DealSize))
    )

stats

write_xlsx(stats, file$rt_sp090_15__vc_related_deals_sum_stats__xl)

# # box plot for DealSize
# # Single box plot
# plt <- ggplot(df, aes(x = "", y = DealSize)) +
#     geom_boxplot(fill = "lightblue", color = "black") +
#     labs(title = "Box Plot", y = "Values") +
#     theme_minimal()
#
# ggsave("boxplot.svg",
#        plot = plt,
#        width = 12,
#        height = 7,
#        dpi = 300)


df_deals_amount_by_yr <- df %>%
    mutate(yr = as.numeric(format(DealDate, "%Y"))) %>%
    group_by(yr) %>%
    summarise(
        total_dealsize = sum(DealSize, na.rm = TRUE),
        mean_dealsize = mean(DealSize, na.rm = TRUE),
        median_dealsize = median(DealSize, na.rm = TRUE),
        count_deals = n()
    )

df_deals_amount_by_yr


df_deals_amount_by_yr <- df_deals_amount_by_yr %>%
    mutate(total_dealsize_billion = total_dealsize / 1000)

df_deals_amount_by_yr



plt_deals_value <- ggplot(df_deals_amount_by_yr, aes(x = yr, y = total_dealsize_billion)) +
    geom_bar(stat = "identity", fill = "#2E86AB", width = 0.7) +
    geom_text(aes(label = sprintf("%.1f", total_dealsize_billion)), vjust = -0.5, size = 3.5, color = "#333333") +
    scale_x_continuous(breaks = df_deals_amount_by_yr$yr) +
    scale_y_continuous(expand = expansion(mult = c(0, 0.1))) +
    labs(title = "Total Deal Values Over Time (in Billions USD)",
         subtitle = paste("Total deals:", sum(df_deals_amount_by_yr$count_deals)),
         x = "Year",
         y = "Total Deals Amount (in Billions USD)") +
    theme_minimal(base_size = 12) +
    theme(
        plot.title = element_text(face = "bold", size = 16, margin = margin(b = 5)),
        plot.subtitle = element_text(size = 11, color = "#666666", margin = margin(b = 15)),
        plot.caption = element_text(size = 9, color = "#999999", hjust = 1),
        axis.title = element_text(face = "bold", size = 11),
        axis.text.x = element_text(angle = 45, hjust = 1, size = 10),
        axis.text.y = element_text(size = 10),
        panel.grid.major.x = element_blank(),
        panel.grid.minor = element_blank(),
        panel.grid.major.y = element_line(color = "#E0E0E0", linewidth = 0.3),
        plot.margin = margin(20, 20, 20, 20)
    )

ggsave(file$rp_sp090_20__deals_amount_by_year__fmt1__pdf,
       plot = plt_deals_value,
       width = 12,
       height = 7,
       dpi = 300)

ggsave(file$rp_sp090_25__deals_amount_by_year__fmt2__svg,
       plot = plt_deals_value,
       width = 12,
       height = 7,
       dpi = 300)



# mean deal value in Millions


plt_mean <- ggplot(df_deals_amount_by_yr, aes(x = yr, y = mean_dealsize)) +
    geom_bar(stat = "identity", fill = "#2E86AB", width = 0.7) +
    geom_text(aes(label = sprintf("%.1f", mean_dealsize)), vjust = -0.5, size = 3.5, color = "#333333") +
    scale_x_continuous(breaks = df_deals_amount_by_yr$yr) +
    scale_y_continuous(expand = expansion(mult = c(0, 0.1))) +
    labs(title = "Mean Deal Values Over Time (in Millions USD)",
         subtitle = paste("Total deals:", sum(df_deals_amount_by_yr$count_deals)),
         x = "Year",
         y = "Mean Deal Size (in Millions USD)") +
    theme_minimal(base_size = 12) +
    theme(
        plot.title = element_text(face = "bold", size = 16, margin = margin(b = 5)),
        plot.subtitle = element_text(size = 11, color = "#666666", margin = margin(b = 15)),
        plot.caption = element_text(size = 9, color = "#999999", hjust = 1),
        axis.title = element_text(face = "bold", size = 11),
        axis.text.x = element_text(angle = 45, hjust = 1, size = 10),
        axis.text.y = element_text(size = 10),
        panel.grid.major.x = element_blank(),
        panel.grid.minor = element_blank(),
        panel.grid.major.y = element_line(color = "#E0E0E0", linewidth = 0.3),
        plot.margin = margin(20, 20, 20, 20)
    )


ggsave(file$rp_sp090_30__deals_mean_amount_by_year__fmt1__pdf,
       plot = plt_mean,
       width = 12,
       height = 7,
       dpi = 300)

ggsave(file$rp_sp090_35__deals_mean_amount_by_year__fmt2__svg,
       plot = plt_mean,
       width = 12,
       height = 7,
       dpi = 300)



# median deal value in Millions



plt_median <- ggplot(df_deals_amount_by_yr, aes(x = yr, y = median_dealsize)) +
    geom_bar(stat = "identity", fill = "#2E86AB", width = 0.7) +
    geom_text(aes(label = sprintf("%.1f", median_dealsize)), vjust = -0.5, size = 3.5, color = "#333333") +
    scale_x_continuous(breaks = df_deals_amount_by_yr$yr) +
    scale_y_continuous(expand = expansion(mult = c(0, 0.1))) +
    labs(title = "Median Deal Size Over Time (in Millions USD)",
         subtitle = paste("Total deals:", sum(df_deals_amount_by_yr$count_deals)),
         x = "Year",
         y = "Median Deal Size (in Millions USD)") +
    theme_minimal(base_size = 12) +
    theme(
        plot.title = element_text(face = "bold", size = 16, margin = margin(b = 5)),
        plot.subtitle = element_text(size = 11, color = "#666666", margin = margin(b = 15)),
        plot.caption = element_text(size = 9, color = "#999999", hjust = 1),
        axis.title = element_text(face = "bold", size = 11),
        axis.text.x = element_text(angle = 45, hjust = 1, size = 10),
        axis.text.y = element_text(size = 10),
        panel.grid.major.x = element_blank(),
        panel.grid.minor = element_blank(),
        panel.grid.major.y = element_line(color = "#E0E0E0", linewidth = 0.3),
        plot.margin = margin(20, 20, 20, 20)
    )


ggsave(file$rp_sp090_40__deals_median_by_year__fmt1__pdf,
       plot = plt_median,
       width = 12,
       height = 7,
       dpi = 300)

ggsave(file$rp_sp090_45__deals_median_by_year__fmt2__svg,
       plot = plt_median,
       width = 12,
       height = 7,
       dpi = 300)



# Pie chart of companies industries

df_c <- read_excel(file$od_c60_20__companies_in_vc_deals__xl)
head(df_c)

table(df_c$PrimaryIndustrySector)

df_sum <- as.data.frame(table(df_c$PrimaryIndustrySector))
names(df_sum) <- c("cat", "count")
df_sum

df_sum <- df_sum %>%
    arrange(desc(count)) %>%  # Sort by count (descending)
    mutate(
        pct = count / sum(count) * 100,
        cat_letter = LETTERS[row_number()],  # A, B, C, etc.
        label = paste0(cat_letter, ": ", round(pct, 1), "%"),
        csum = rev(cumsum(rev(count))),
        pos = count/2 + lead(csum, 1),
        pos = if_else(is.na(pos), count/2, pos),
        cat = factor(cat, levels = cat)  # Fix the factor levels to match sorted order
    )

df_sum


pie_chart <- ggplot(df_sum, aes(x = "", y = count, fill = cat)) +
    geom_bar(stat = "identity", width = 1, color = "white") +
    coord_polar("y", start = 0) +
    geom_label_repel(aes(y = pos, label = label),
                     nudge_x = 0.7,
                     show.legend = FALSE,
                     size = 4,
                     segment.color = "grey40") +
    theme_void() +
    theme(
        legend.position = "right",
        legend.title = element_text(size = 14, face = "bold", margin = margin(b = 10)),
        legend.text = element_text(size = 11, margin = margin(l = 5)),
        legend.key.size = unit(1, "cm"),
        plot.title = element_text(hjust = 0.5, size = 18, face = "bold", margin = margin(b = 20)),
        plot.subtitle = element_text(hjust = 0.5, size = 12, color = "grey40", margin = margin(b = 20)),
        plot.margin = margin(20, 20, 20, 20),
        plot.background = element_rect(fill = "white", color = NA),
        panel.background = element_rect(fill = "white", color = NA)
    ) +
    labs(
        fill = "Categories",
        title = "Distribution by Category",
        subtitle = paste0("Total: ", format(sum(df_sum$count), big.mark = ","))
    ) +
    scale_fill_brewer(palette = "Set3",
                      labels = paste0(df_sum$cat_letter, ": ", df_sum$cat, " (#", df_sum$count, ", ", round(df_sum$pct, 1), "%)"))


ggsave(file$rp_sp090_50__invested_industries__fmt1__pdf,
       plot = pie_chart,
       width = 12,
       height = 6,
       dpi = 300)

ggsave(file$rp_sp090_55__invested_industries__fmt2__svg,
       plot = pie_chart,
       width = 12,
       height = 6,
       dpi = 300)
